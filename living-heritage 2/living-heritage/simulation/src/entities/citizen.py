"""
Citizen entity for the Living Heritage simulation engine.

A Citizen is the basic "agent" of the simulation. Each citizen has:
  - a basic identity (id, name, age, gender)
  - family links (parents, spouse, children)
  - an economic life (job, income)
  - an education level
  - cultural knowledge (which traditions they know, and how well)

Design notes for the team:
  - This module has NO dependencies on the database, the backend, or any
    other part of the system. It should stay usable and testable on its
    own — that's what keeps the simulation "explainable".
  - Family links are stored as IDs (not direct object references) so a
    Citizen can be saved/loaded (e.g. to JSON or a database row) without
    circular-reference headaches.
  - Cultural knowledge is a simple 0-100 "proficiency" score per
    tradition. The "cultural transmission" build step (later) will decide
    the *rules* for how proficiency grows (learning from a parent, a
    festival, a mentor, etc.) — this class just stores the number and
    offers a safe way to increase it.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional
import itertools


class EducationLevel(Enum):
    """How far a citizen has gone in formal education."""

    NONE = "none"
    PRIMARY = "primary"
    SECONDARY = "secondary"
    HIGHER = "higher"


# A simple auto-incrementing counter so every citizen gets a unique,
# easy-to-read integer id (1, 2, 3, ...) instead of a long random string.
# This is intentionally simple for an MVP — if we ever need to create
# citizens across multiple processes at once, this will need to change.
_id_counter = itertools.count(1)


def _next_id() -> int:
    return next(_id_counter)


@dataclass
class Citizen:
    """A single resident of the town."""

    name: str
    age: int
    gender: str  # free text ("male" / "female" / "other") — kept simple for the MVP
    id: int = field(default_factory=_next_id)

    # --- Family links (store IDs, not Citizen objects) ---
    mother_id: Optional[int] = None
    father_id: Optional[int] = None
    spouse_id: Optional[int] = None
    children_ids: List[int] = field(default_factory=list)

    # --- Economic life ---
    occupation: Optional[str] = None
    income: float = 0.0

    # --- Education ---
    education_level: EducationLevel = EducationLevel.NONE

    # --- Cultural knowledge: tradition_id -> proficiency (0-100) ---
    cultural_knowledge: Dict[str, float] = field(default_factory=dict)

    # ---------------- Helper methods ----------------

    def is_adult(self, adult_age: int = 18) -> bool:
        """True once the citizen is old enough to work / marry / vote."""
        return self.age >= adult_age

    def is_employed(self) -> bool:
        return self.occupation is not None

    def knows_tradition(self, tradition_id: str) -> bool:
        """True if the citizen has any proficiency at all in this tradition."""
        return tradition_id in self.cultural_knowledge

    def knowledge_of(self, tradition_id: str) -> float:
        """Proficiency (0-100) in a tradition. 0 if never learned."""
        return self.cultural_knowledge.get(tradition_id, 0.0)

    def learn_tradition(self, tradition_id: str, amount: float) -> None:
        """
        Increase this citizen's proficiency in a tradition by `amount`
        points, capped at 100.

        This is the basic building block that the "cultural transmission"
        step will call whenever a citizen learns from a practitioner, a
        parent, a festival, or a class.
        """
        if amount < 0:
            raise ValueError("amount must be non-negative")
        current = self.cultural_knowledge.get(tradition_id, 0.0)
        self.cultural_knowledge[tradition_id] = min(100.0, current + amount)

    def add_child(self, child_id: int) -> None:
        """Link a child to this citizen (no-op if already linked)."""
        if child_id not in self.children_ids:
            self.children_ids.append(child_id)

    def __repr__(self) -> str:
        return (
            f"Citizen(id={self.id}, name={self.name!r}, age={self.age}, "
            f"occupation={self.occupation!r}, "
            f"education={self.education_level.value})"
        )
