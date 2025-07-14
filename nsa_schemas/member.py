"""Pydantic schemas for the Member entity in the PostgreSQL microservice."""

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, ConfigDict
from nsa_schemas.availability import AvailabilityInDB

# pylint: disable=too-few-public-methods
class MemberBase(BaseModel):
    """Base class for member schemas with shared fields."""

    discord_id: str
    pseudo: str
    role: Optional[str] = None
    team_id: Optional[int] = None
    is_active: Optional[bool] = True


class MemberCreate(MemberBase):
    """Schema for creating a new member."""


class MemberUpdate(BaseModel):
    """Schema for updating an existing member."""

    pseudo: Optional[str] = None
    role: Optional[str] = None
    team_id: Optional[int] = None
    is_active: Optional[bool] = None


class MemberOut(MemberBase):
    """Schema for returning a member with metadata and availabilities."""

    id: int
    joined_at: datetime
    availabilities: List[AvailabilityInDB] = []

    model_config = ConfigDict(from_attributes=True)
