"""Pydantic schemas for the Planning and Availability entities in the PostgreSQL microservice and business layer.

Ce fichier contient :
- Les modèles BDD pour plannings (Create, Update, Out)
- Les modèles métier pour la génération des plannings joueur (Input, Generated)
"""

from datetime import datetime
from typing import Dict, Optional, List

from pydantic import BaseModel, ConfigDict


# ============================
# SCHEMAS PLANNING (BDD TEAM)
# ============================

class PlanningBase(BaseModel):
    """Base class with shared planning fields (BDD)."""
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


# ============================
# SCHEMAS METIER (DISPOS JOUEUR)
# ============================

class PlanningInput(BaseModel):
    """Entrée utilisateur pour remplir les disponibilités d'un joueur (logique métier)."""

    player_id: str
    team: str
    date: str  # Format JJ/MM (ex: "08/07")
    days: List[str]  # Liste des jours renseignés (ex: ["lundi", "mardi"])
    value: str  # Disponibilité renseignée (ex: "21h")


class PlanningGenerated(BaseModel):
    """Planning hebdomadaire généré pour un joueur avec disponibilités complètes."""

    player_id: str
    team: str
    week_start: str  # Date ISO du lundi (YYYY-MM-DD)
    entries: Dict[str, str]  # {date_iso: "21h" ou "Indéterminée"}
