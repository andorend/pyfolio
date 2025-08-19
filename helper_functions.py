import random
import webcolors
import yaml
from bs4 import BeautifulSoup
from pydantic import ValidationError
from models import PortfolioModel


def prettify_html(html: str) -> str:
    """
    Create beautiful HTML using BeautifulSoup
    
    :param html: The input raw HTML
    :return: The beautiful HTML
    """
    
    try:
        soup = BeautifulSoup(html, 'html.parser')
        return soup.prettify()
    except Exception as e:
        # If BeautifulSoup fails, return the original HTML
        # This provides a fallback in case of compatibility issues
        print(f"Warning: BeautifulSoup prettify failed ({e}), returning original HTML")
        return html


def load_yaml_portfolio(path: str = "portfolio.yaml") -> PortfolioModel:
    """
    Load and validate the YAML portfolio data using Pydantic.
    
    :param path: path of the YAML file
    :return: the validated PortfolioModel instance containing the portfolio
    :raises ValidationError: if the YAML data doesn't match the expected schema
    :raises FileNotFoundError: if the YAML file doesn't exist
    :raises yaml.YAMLError: if the YAML file is malformed
    """
    
    try:
        with open(path, "r", encoding="utf-8") as f:
            raw_data = yaml.safe_load(f)
        
        # Validate and parse the data using Pydantic
        portfolio = PortfolioModel(**raw_data)
        return portfolio
        
    except FileNotFoundError:
        raise FileNotFoundError(f"Portfolio file not found: {path}")
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Error parsing YAML file {path}: {e}")
    except ValidationError as e:
        raise ValidationError(f"Portfolio data validation failed: {e}")


def load_portfolio_as_dict(path: str = "portfolio.yaml") -> dict:
    """
    Load the YAML portfolio data and return as a dictionary for backward compatibility.
    
    :param path: path of the YAML file
    :return: the portfolio data as a dictionary
    """
    portfolio_model = load_yaml_portfolio(path)
    # Convert Pydantic model to dictionary, handling nested models and URL objects
    return portfolio_model.model_dump(mode='python')


def int_to_hex(i: int) -> str:
    """
    Convert the input integer (0-255) to a two digit hexadecimal string.

    :param i: integer between 0-255
    :return: the two digit hexadecimal representation of the input integer

    Example:
    >>> int_to_hex(10)
    '0A'
    """
    return f"{i:02X}"

def randomize_color(color: str, color_shift_percentage: int = 1) -> str:
    """
    Shift the colors by a percentage but only change the luminosity of the color.

    :param color: Color string in any HTML5 format
    :param color_shift_range: The range in which the color should shift in percentage
    :return: The shifted color in #RRGGBB hex color format

    Examples:
    >>> randomize_color("#506080", 10)
    '#495875'

    >>> randomize_color("purple", 25)
    '#680068'

    >>> randomize_color("rgb(200,200,200)", 3)
    '#C5C5C5'
    """

    # The webcolors module handles badly the rgb colors:
    if color[:3].lower() == "rgb":
        webcolor = list(map(int, color[4:-1].split(",")))
    # Let the webcolors handle the other cases
    else:
        webcolor = list(webcolors.html5_parse_legacy_color(color).__iter__())

    random_shift = 1 - random.random() * (color_shift_percentage / 100)
    return "#" + "".join(int_to_hex(min(255, max(0, round(base_color * random_shift)))) for base_color in webcolor)


# Run doctests
if __name__ == "__main__":
    import doctest
    random.seed(0)
    doctest.testmod()
