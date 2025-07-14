"""Unit tests for the Planning schemas."""

from datetime import UTC, datetime
from nsa_schemas import PlanningCreate, PlanningUpdate, PlanningOut


def test_planning_create():
    """Test creating a planning using PlanningCreate."""
    planning = PlanningCreate(team_id=1, week=28, year=2025)
    assert planning.team_id == 1
    assert planning.week == 28


def test_planning_update():
    """Test updating a planning using PlanningUpdate."""
    update = PlanningUpdate(description="Test planning")
    assert update.description == "Test planning"


def test_planning_out():
    """Test returning a planning with metadata using PlanningOut."""
    planning = PlanningOut(
        id=1,
        team_id=1,
        week=28,
        year=2025,
        created_at=datetime.now(UTC)
    )
    assert planning.id == 1
