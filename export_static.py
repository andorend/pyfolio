"""
Export Pyfolio website as static standalone HTML
"""
import os
import random
from flask import Flask, render_template
from helper_functions import load_yaml_portfolio, prettify_html, randomize_color


def export_static_html():
    """Export the portfolio website as a standalone HTML file"""
    
    try:
        # Set random seed for consistent but varied colors
        random.seed(42)  # You can change this seed for different color variations
        
        # Load portfolio data
        portfolio_data = load_yaml_portfolio("portfolio.yaml")
        
        # Create a new Flask app for static export
        static_app = Flask(__name__)
        static_app.config['SERVER_NAME'] = 'localhost'
        
        # Add the randomize_color function to template globals
        static_app.jinja_env.globals.update(randomize_color=randomize_color)
        
        # Create application context for rendering
        with static_app.app_context():
            with static_app.test_request_context():
                # Render the portfolio template with data
                rendered_html = render_template('portfolio.html', portfolio=portfolio_data)
        
        # Prettify the HTML
        pretty_html = prettify_html(rendered_html)
        
        # Read CSS and JS files
        css_content = ""
        js_content = ""
        
        css_path = os.path.join('static', 'style.css')
        js_path = os.path.join('static', 'portfolio.js')
        
        if os.path.exists(css_path):
            with open(css_path, 'r', encoding='utf-8') as f:
                css_content = f.read()
        
        if os.path.exists(js_path):
            with open(js_path, 'r', encoding='utf-8') as f:
                js_content = f.read()
        
        # Create standalone HTML with embedded CSS and JS
        standalone_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pyfolio - Andor Hofecker</title>
    <style>
{css_content}
    </style>
</head>
<body>
{pretty_html[pretty_html.find('<body>') + 6:pretty_html.find('</body>')]}
    <script>
{js_content}
    </script>
</body>
</html>"""
        
        # Save the standalone HTML file
        output_file = "pyfolio_standalone.html"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(standalone_html)
        
        print(f"✅ Static HTML exported successfully to: {output_file}")
        print(f"📁 File size: {os.path.getsize(output_file) / 1024:.1f} KB")
        print(f"🌐 You can open this file directly in any web browser")
        
        return output_file
        
    except Exception as e:
        print(f"❌ Error exporting static HTML: {e}")
        raise


if __name__ == "__main__":
    export_static_html()
