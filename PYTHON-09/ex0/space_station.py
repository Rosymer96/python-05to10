from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    """Model to validate space station information."""
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime = ...
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)


def print_station_info(s: SpaceStation) -> None:
    """Display formatted space station information."""
    print(f"ID: {s.station_id}")
    print(f"Name: {s.name}")
    print(f"Crew: {s.crew_size} people")
    print(f"Power: {s.power_level}%")
    print(f"Oxygen: {s.oxygen_level}%")
    print(f"Last maintenance: {s.last_maintenance}")
    print(f"Status: "
          f"{'Operational' if s.is_operational else 'Not Operational'}")
    if s.notes:
        print(f"Notes: {s.notes}")
    print()


def main() -> None:
    """Demonstrate valid and invalid station validation."""
    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")
    try:
        valid_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2023-07-11T00:00:00"
        )
        print_station_info(valid_station)
    except ValidationError as e:
        print(e)
    print("========================================")
    print("Expected validation error:")
    try:
        invalid_station = SpaceStation(
            station_id="ISS002",
            name="Apollo 11",
            crew_size=25,
            power_level=80.0,
            oxygen_level=95.0,
            last_maintenance=datetime.now(),
            is_operational=False,
        )
        print_station_info(invalid_station)
    except ValidationError as e:
        errors = e.errors()
        for error in errors:
            print(f"{error['msg']}")


if __name__ == "__main__":
    main()
