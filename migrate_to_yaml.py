"""
Migration script to convert existing JSON portfolio to YAML format with Pydantic validation.
"""

import json
import yaml
from models import PortfolioModel
from pydantic import ValidationError


def migrate_json_to_yaml(json_path: str = "portfolio.json", yaml_path: str = "portfolio.yaml"):
    """
    Migrate portfolio data from JSON to YAML format with validation.
    
    :param json_path: Path to the existing JSON file
    :param yaml_path: Path for the new YAML file
    """
    
    try:
        # Load existing JSON data
        print(f"📖 Loading JSON data from {json_path}...")
        with open(json_path, "r", encoding="utf-8") as f:
            json_data = json.load(f)
        
        # Validate data using Pydantic
        print("🔍 Validating data structure...")
        portfolio_model = PortfolioModel(**json_data)
        print("✅ Data validation successful!")
        
        # Write to YAML format
        print(f"📝 Writing YAML data to {yaml_path}...")
        with open(yaml_path, "w", encoding="utf-8") as f:
            yaml.dump(json_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
        
        print("✅ Migration completed successfully!")
        print(f"🎉 Portfolio data has been migrated from {json_path} to {yaml_path}")
        
        # Validate the written YAML file can be loaded
        print("🔍 Verifying YAML file integrity...")
        with open(yaml_path, "r", encoding="utf-8") as f:
            yaml_data = yaml.safe_load(f)
        
        # Ensure the data is still valid
        PortfolioModel(**yaml_data)
        print("✅ YAML file verification successful!")
        
    except FileNotFoundError as e:
        print(f"❌ File not found: {e}")
        raise
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON format: {e}")
        raise
    except ValidationError as e:
        print(f"❌ Data validation failed: {e}")
        raise
    except yaml.YAMLError as e:
        print(f"❌ YAML processing error: {e}")
        raise
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        raise


if __name__ == "__main__":
    migrate_json_to_yaml()
