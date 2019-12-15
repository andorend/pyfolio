from flask import Flask, render_template
import os

from helper_functions import randomize_color, load_json_portfolio, prettify_html

app = Flask(__name__)

portfolio = load_json_portfolio()

@app.route('/')
def portfolio_page(name: str = "pytfolio") -> str:
    """
    The main page of the pytfolio.

    :param name: The name of the page
    :return: rendered, beautiful HTML
    """

    return prettify_html(render_template('portfolio.html',
                                         portfolio=portfolio,
                                         randomize_color=randomize_color,
                                         features="html.parser"))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
