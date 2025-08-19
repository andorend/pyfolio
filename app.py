import os

from flask import Flask, render_template
from helper_functions import randomize_color, load_portfolio_as_dict, prettify_html

app = Flask(__name__)

portfolio = load_portfolio_as_dict()


@app.route("/")
def portfolio_page(name: str = "pyfolio") -> str:
    """
    The main page of the pyfolio.

    :param name: The name of the page
    :return: rendered, beautiful HTML
    """

    return prettify_html(
        render_template(
            "portfolio.html",
            portfolio=portfolio,
            randomize_color=randomize_color,
            features="html.parser",
        )
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="localhost", port=port)
