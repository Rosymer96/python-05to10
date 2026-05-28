from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    """Available crew ranks."""
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """Model representing an individual crew member."""
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank = ...
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    """Model to validate space mission requirements."""
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime = ...
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission_rules(self) -> 'SpaceMission':
        """Validate mission safety and crew requirements."""
        if not self.mission_id.startswith("M"):
            raise ValueError(
                "Mission ID must start with 'M'"
                )
        ranks = {Rank.COMMANDER, Rank.CAPTAIN}
        has_ranks = any(member.rank in ranks for member in self.crew)
        if not has_ranks:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
                )
        if self.duration_days > 365:
            experienced_total = sum(
                1 for member in self.crew if member.years_experience > 5
            )
            experience_ratio = experienced_total / len(self.crew)
            if experience_ratio < 0.5:
                raise ValueError(
                    "Long missions over 1 year require at least 50% "
                    "experienced crew (5+ years). Current"
                )
            someone_inactive = any(
                not member.is_active for member in self.crew
                )
            if someone_inactive:
                raise ValueError(
                    "All crew members must be active for missions"
                    " longer than 1 year"
                )
        return self


def print_mission_info(m: SpaceMission) -> None:
    """Display formatted mission information."""
    print(f"Mission: {m.mission_name}")
    print(f"ID: {m.mission_id}")
    print(f"Destination: {m.destination}")
    print(f"Duration: {m.duration_days} days")
    print(f"Budget: ${m.budget_millions:.1f}M")
    print(f"Crew size: {len(m.crew)}")
    print("crew members:")
    for member in m.crew:
        print(f"- {member.name} ({member.rank.value})"
              f" - {member.specialization}")
    print()


def main() -> None:
    """Demonstrate valid and invalid mission validation."""
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    try:
        valid_crew = [
            CrewMember(
                member_id="SC001",
                name="Sarah Connor",
                rank=Rank.COMMANDER,
                age=45,
                specialization="Mission Command",
                years_experience=20
            ),
            CrewMember(
                member_id="JS002",
                name="John Smith",
                rank=Rank.LIEUTENANT,
                age=35,
                specialization="Navigation",
                years_experience=10
            ),
            CrewMember(
                member_id="AJ003",
                name="Alice Johnson",
                rank=Rank.OFFICER,
                age=28,
                specialization="Engineering",
                years_experience=6
            ),
        ]

        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 6, 15, 9, 0, 0),
            duration_days=900,
            crew=valid_crew,
            budget_millions=2500.0
        )
        print_mission_info(valid_mission)
    except ValidationError as e:
        for error in e.errors():
            print(f"{error['msg']}")

    print("=========================================")
    print("Expected validation error:")
    try:
        invalid_crew = [
            CrewMember(
                member_id="CD001",
                name="Mike Wilson",
                rank=Rank.CADET,
                age=22,
                specialization="Research",
                years_experience=1
            ),
            CrewMember(
                member_id="OF002",
                name="Jane Doe",
                rank=Rank.OFFICER,
                age=30,
                specialization="Communications",
                years_experience=4
            ),
        ]

        SpaceMission(
            mission_id="M2024_MOON",
            mission_name="Lunar Survey",
            destination="Moon",
            launch_date=datetime(2024, 8, 1, 10, 0, 0),
            duration_days=30,
            crew=invalid_crew,
            budget_millions=500.0
        )
    except ValidationError as e:
        for error in e.errors():
            print(f"{error['msg']}")


if __name__ == "__main__":
    main()
