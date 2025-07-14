"""Unit tests for the Team schemas."""

from datetime import UTC, datetime
from nsa_schemas import TeamCreate, TeamUpdate, TeamOut


def test_team_create():
    """Test creating a team using TeamCreate."""
    team = TeamCreate(name="Never Sleep Again", tag="NSA")
    assert team.name == "Never Sleep Again"
    assert team.tag == "NSA"
    assert team.logo is None


def test_team_update():
    """Test updating a team using TeamUpdate."""
    update = TeamUpdate(name="New Name")
    assert update.name == "New Name"
    assert update.tag is None


def test_team_out():
    """Test returning a team with metadata using TeamOut."""
    now = datetime.now(UTC)
    team = TeamOut(id=1, name="NSA", tag="NSA", logo=None, created_at=now)
    assert team.id == 1
    assert team.created_at == now
