"""Unit tests for the Member schemas."""

from datetime import UTC, datetime, date
from nsa_schemas import MemberCreate, MemberUpdate, MemberOut, AvailabilityInDB


def test_member_create():
    """Test creating a member using MemberCreate."""
    member = MemberCreate(discord_id="123456789", pseudo="Rhodu", role="Capitaine")
    assert member.discord_id == "123456789"
    assert member.pseudo == "Rhodu"
    assert member.role == "Capitaine"
    assert member.is_active is True


def test_member_update():
    """Test updating a member using MemberUpdate."""
    update = MemberUpdate(pseudo="NewPseudo", is_active=False)
    assert update.pseudo == "NewPseudo"
    assert update.is_active is False


def test_member_out():
    """Test returning a member with metadata and availabilities using MemberOut."""
    availability = AvailabilityInDB(id=1, member_id=1, day=date.today(), value="21h")
    member = MemberOut(
        id=1,
        discord_id="123456789",
        pseudo="Rhodu",
        role="Capitaine",
        team_id=1,
        is_active=True,
        joined_at=datetime.now(UTC),
        availabilities=[availability]
    )
    assert member.availabilities[0].value == "21h"
