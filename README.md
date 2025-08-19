# pyfolio
My own portfolio app using YAML as input with Pydantic validation, Python Flask for backend, Jinja2 HTML template for processing the YAML input. And a bit of CSS with Flexboxes for the visuals and Javascript for interactivity.

## New Features (v2.0)
- ✨ **YAML Configuration**: Portfolio data is now stored in `portfolio.yaml` for better readability
- 🔧 **Pydantic Validation**: Strong data validation and type checking using Pydantic models  
- 🛡️ **Error Handling**: Comprehensive error handling for malformed data
- 📝 **Better Documentation**: Enhanced docstrings and type hints
- 🔄 **Migration Support**: Automatic migration from JSON to YAML format

## Data Structure Validation
The portfolio data is now validated using Pydantic models that ensure:
- ✅ Required fields are present
- ✅ URL fields contain valid URLs
- ✅ Date formats are correct
- ✅ Project groups have corresponding styling definitions
- ✅ Tags are not empty
- ✅ Color formats are valid

To test/run the Flask app in Windows:
- cd into the pyfolio/pyfolio folder (using Command Prompt)
- Install dependencies: `pip install -r requirements.txt`
- Run the following commands:

    - ```set FLASK_APP=app.py```

    - ```flask run```

- Open the shown link in the browser.

## Migration from JSON
If you have an existing `portfolio.json` file, you can migrate it to YAML format:
```bash
python migrate_to_yaml.py
```

## Data Files
- `portfolio.yaml` - Main portfolio data in YAML format
- `models.py` - Pydantic models for data validation
- `portfolio.py` - Python data structure (can generate YAML)

- Working demo: https://pyfolio-andor-hofecker.herokuapp.com/

Feel free to fork but do not use my personal information.