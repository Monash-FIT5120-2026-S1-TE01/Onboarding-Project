"""
For pydantic models
"""
from pydantic import BaseModel
from typing import List

class RecommendQuery(BaseModel):
    uv_level: float