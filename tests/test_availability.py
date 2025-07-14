"""Unit tests for the Availability schemas."""

from datetime import date
from nsa_schemas import AvailabilityCreate, AvailabilityUpdate, AvailabilityUpsert, AvailabilityInDB


def test_availability_create():
    """Test creating an availability using AvailabilityCreate."""
    availability = AvailabilityCreate(day=date.today(), value="21h", member_id=1)
    assert availability.value == "21h"
    assert availability.member_id == 1


def test_availability_update():
    """Test updating an availability using AvailabilityUpdate."""
    update = AvailabilityUpdate(day=date.today(), value="18h")
    assert update.value == "18h"


def test_availability_upsert():
    """Test upserting an availability using AvailabilityUpsert."""
    upsert = AvailabilityUpsert(value="Indisponible")
    assert upsert.value == "Indisponible"


def test_availability_in_db():
    """Test availability stored in DB using AvailabilityInDB."""
    avail = AvailabilityInDB(id=1, member_id=1, day=date.today(), value="21h")
    assert avail.id == 1
    assert avail.value == "21h"
