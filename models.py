from typing import Dict, List, Optional
from pydantic import BaseModel, HttpUrl, Field, field_validator


class PersonModel(BaseModel):
    """Pydantic model for person information"""
    name: str = Field(..., min_length=1, description="Full name of the person")
    birth: str = Field(..., description="Birth date in DD.MM.YYYY format")
    nation: str = Field(..., min_length=2, max_length=2, description="Nation code (e.g., HU)")
    image: Optional[HttpUrl] = Field(None, description="URL to profile image")
    contact_info: Dict[str, str] = Field(..., description="Contact information dictionary")
    languages: Dict[str, str] = Field(..., description="Languages and proficiency levels")
    hobbies: List[str] = Field(..., description="List of hobbies")

    @field_validator('birth')
    @classmethod
    def validate_birth_format(cls, v):
        """Validate birth date format DD.MM.YYYY"""
        import re
        if not re.match(r'^\d{2}\.\d{2}\.\d{4}$', v):
            raise ValueError('Birth date must be in DD.MM.YYYY format')
        return v

    @field_validator('nation')
    @classmethod
    def validate_nation_uppercase(cls, v):
        """Ensure nation code is uppercase"""
        return v.upper()


class ProjectModel(BaseModel):
    """Pydantic model for project information"""
    title: str = Field(..., min_length=1, description="Project title")
    supertitle: Optional[str] = Field(None, description="Project supertitle (e.g., year)")
    subtitle: Optional[str] = Field(None, description="Project subtitle or role")
    group: str = Field(..., min_length=1, description="Project category/group")
    link: Optional[HttpUrl] = Field(None, description="URL to project or related information")
    image: Optional[HttpUrl] = Field(None, description="URL to project image")
    highlighted: bool = Field(False, description="Whether this project is highlighted")
    tags: List[str] = Field(..., min_items=1, description="List of technology/skill tags")

    @field_validator('tags')
    @classmethod
    def validate_tags_not_empty(cls, v):
        """Ensure tags list is not empty and contains valid strings"""
        if not v:
            raise ValueError('Tags list cannot be empty')
        return [tag.strip() for tag in v if tag.strip()]


class GroupModel(BaseModel):
    """Pydantic model for project group styling"""
    text_color: str = Field(..., description="Text color for the group")
    bg_color: str = Field(..., description="Background color for the group")

    @field_validator('text_color', 'bg_color')
    @classmethod
    def validate_color_format(cls, v):
        """Validate color format (hex, rgb, or named colors)"""
        import re
        # Allow hex colors, rgb colors, and named colors
        hex_pattern = r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'
        rgb_pattern = r'^rgb\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*\)$'
        
        if not (re.match(hex_pattern, v) or re.match(rgb_pattern, v) or 
                v.lower() in ['white', 'black', 'red', 'green', 'blue', 'yellow', 
                             'purple', 'orange', 'pink', 'brown', 'gray', 'grey']):
            # For more complex validation, we could use webcolors here
            pass  # Allow any string for now, as webcolors will validate during processing
        return v


class PortfolioModel(BaseModel):
    """Main Pydantic model for the entire portfolio"""
    person: PersonModel = Field(..., description="Personal information")
    projects: List[ProjectModel] = Field(..., min_items=1, description="List of projects")
    groups: Dict[str, GroupModel] = Field(..., description="Project group styling definitions")

    @field_validator('groups')
    @classmethod
    def validate_project_groups_exist(cls, v, info):
        """Ensure all project groups have corresponding group definitions"""
        # In Pydantic v2, we need to use info.data to access other field values
        if info.data and 'projects' in info.data:
            project_groups = {project.group for project in info.data['projects']}
            missing_groups = project_groups - set(v.keys())
            if missing_groups:
                raise ValueError(f'Missing group definitions for: {missing_groups}')
        return v

    class Config:
        # Allow validation of URLs
        str_strip_whitespace = True
        validate_assignment = True
