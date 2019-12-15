import random
import webcolors
import json
from bs4 import BeautifulSoup


def prettify_html(html: str) -> str:
    """
    Create beautiful HTML using BeautifulSoup

    :param html: The input raw HTML
    :return: The beautiful HTML
    """

    soup = BeautifulSoup(html)
    return soup.prettify()


def load_json_portfolio(path: str = "portfolio.json") -> dict:
    """
    Load the the json data as a dict.
    :param path: path of the json
    :return: the dict containing the portfolio
    """

    with open("portfolio.json", "r") as f:
        return json.loads(f.read())


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
