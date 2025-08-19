"""
Load portfolio from yaml directly
"""


if __name__ == "__main__":
    from helper_functions import load_yaml_portfolio

    portfolio_path = "portfolio.yaml"

    # Create and validate the portfolio using Pydantic
    try:
        loaded_portfolio = load_yaml_portfolio(portfolio_path)
        print("✅ YAML file loads and validates correctly!")
               
    except Exception as e:
        print(f"❌ Error: {e}")
        raise
