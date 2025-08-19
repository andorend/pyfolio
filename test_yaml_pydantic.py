"""
Test file to demonstrate Pydantic validation and YAML loading functionality.
"""

from helper_functions import load_yaml_portfolio, load_portfolio_as_dict
from models import PortfolioModel
from pydantic import ValidationError
import yaml


def test_yaml_loading():
    """Test that the YAML file loads correctly"""
    print("🧪 Testing YAML loading...")
    try:
        portfolio = load_yaml_portfolio("portfolio.yaml")
        print(f"✅ Successfully loaded portfolio for {portfolio.person.name}")
        print(f"📊 Portfolio contains {len(portfolio.projects)} projects")
        print(f"🎨 Portfolio has {len(portfolio.groups)} project groups")
        return True
    except Exception as e:
        print(f"❌ YAML loading failed: {e}")
        return False


def test_data_validation():
    """Test data validation with invalid data"""
    print("\n🧪 Testing data validation with invalid data...")

    # Test with missing required field
    invalid_data = {
        "person": {
            "name": "Test Person",
            # Missing birth date
            "nation": "US",
            "contact_info": {},
            "languages": {},
            "hobbies": [],
        },
        "projects": [],
        "groups": {},
    }

    try:
        PortfolioModel(**invalid_data)
        print("❌ Validation should have failed!")
        return False
    except ValidationError as e:
        print(f"✅ Validation correctly caught error: {str(e).split('1 validation error')[0]}...")
        return True


def test_backward_compatibility():
    """Test backward compatibility function"""
    print("\n🧪 Testing backward compatibility...")
    try:
        portfolio_dict = load_portfolio_as_dict("portfolio.yaml")
        print(f"✅ Successfully converted to dict format")
        print(f"📝 Person name: {portfolio_dict['person']['name']}")
        return True
    except Exception as e:
        print(f"❌ Backward compatibility failed: {e}")
        return False


def test_yaml_structure():
    """Test that YAML structure matches expected format"""
    print("\n🧪 Testing YAML structure...")
    try:
        with open("portfolio.yaml", "r", encoding="utf-8") as f:
            raw_data = yaml.safe_load(f)

        # Check main sections exist
        required_sections = ["person", "projects", "groups"]
        for section in required_sections:
            if section not in raw_data:
                print(f"❌ Missing required section: {section}")
                return False

        # Check person section
        person = raw_data["person"]
        required_person_fields = ["name", "birth", "nation", "contact_info", "languages", "hobbies"]
        for field in required_person_fields:
            if field not in person:
                print(f"❌ Missing person field: {field}")
                return False

        print("✅ YAML structure is valid")
        return True

    except Exception as e:
        print(f"❌ YAML structure test failed: {e}")
        return False


if __name__ == "__main__":
    print("🚀 Running Pyfolio YAML & Pydantic Tests\n")

    tests = [
        test_yaml_structure,
        test_yaml_loading,
        test_data_validation,
        test_backward_compatibility,
    ]

    results = []
    for test in tests:
        results.append(test())

    print(f"\n📈 Test Results: {sum(results)}/{len(results)} tests passed")

    if all(results):
        print("🎉 All tests passed! The YAML/Pydantic integration is working correctly.")
    else:
        print("⚠️  Some tests failed. Please check the implementation.")
