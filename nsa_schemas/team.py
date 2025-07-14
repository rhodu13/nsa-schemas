"""Pydantic schemas for the Team entity in the PostgreSQL microservice."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


# pylint: disable=too-few-public-methods
class TeamBase(BaseModel):
    """Base class for team schemas with common fields."""

    name: str
    tag: str
    logo: Optional[str] = None


class TeamCreate(TeamBase):
    """Schema for creating a new team."""


class TeamUpdate(BaseModel):
    """Schema for updating an existing team."""

    name: Optional[str] = None
    tag: Optional[str] = None
    logo: Optional[str] = None


class TeamOut(TeamBase):
    """Schema for returning a team with metadata."""

    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
