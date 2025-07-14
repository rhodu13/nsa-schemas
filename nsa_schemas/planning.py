"""Pydantic schemas for the Planning entity in the PostgreSQL microservice."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class PlanningBase(BaseModel):
    """Base class with shared planning fields."""
    google_sheet_id: Optional[str] = None
    team_id: int
    week: int
    year: int
    description: Optional[str] = None


class PlanningCreate(PlanningBase):
    """Schema used when creating a planning."""


class PlanningUpdate(BaseModel):
    """Schema for updating planning metadata."""
    google_sheet_id: Optional[str] = None
    description: Optional[str] = None


class PlanningOut(PlanningBase):
    """Schema returned when querying a planning."""

    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
