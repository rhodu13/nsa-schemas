"""Pydantic schemas for Availability model and operations."""

from datetime import date
from pydantic import BaseModel, ConfigDict, Field


class AvailabilityBase(BaseModel):
    """
    Shared base schema for an availability entry.

    Fields:
        day (date): The date of the availability.
        value (str): The availability value (e.g., "21h", "Indisponible").
    """
    day: date = Field(..., description="Date of availability")
    value: str = Field(..., description="Availability value (e.g. '21h', 'Indisponible')")


class AvailabilityCreate(AvailabilityBase):
    """
    Schema for creating a new availability.

    Fields:
        member_id (int): The ID of the member for whom the availability is created.
    """
    member_id: int = Field(..., description="ID of the member this availability belongs to")


class AvailabilityUpdate(AvailabilityBase):
    """
    Schema for updating an existing availability.

    This schema is used when updating an availability by its ID.
    """


class AvailabilityUpsert(BaseModel):
    """
    Schema for upserting (create or update) an availability by member and day.

    Only the value is required, since member_id and day are passed in the route.
    
    Fields:
        value (str): The new availability value to set.
    """
    value: str = Field(..., description="New availability value (e.g. '18h', 'Indisponible')")


class AvailabilityInDB(AvailabilityBase):
    """
    Schema representing an availability as stored in the database.

    Fields:
        id (int): Unique identifier of the availability.
        member_id (int): ID of the member associated with this availability.
    """
    id: int
    member_id: int

    model_config = ConfigDict(from_attributes=True)
