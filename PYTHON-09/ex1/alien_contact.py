from pydantic import BaseModel, model_validator, Field, ValidationError
from datetime import datetime
from enum import Enum


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validate_contact_rules(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError(
                "Contact ID must start with 'AC'"
                )
        if (
            self.contact_type == ContactType.PHYSICAL
            and not self.is_verified
                ):
            raise ValueError(
                "Physical contacts report must be verified"
            )
        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
                ):

            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
                )
        if (self.signal_strength > 7.0 and not self.message_received):
            raise ValueError(
                "Strong signals highter than 7.0 must have a message received"
                )
        return self


def print_contact_info(a: AlienContact) -> None:
    print(f"ID: {a.contact_id}")
    print(f"Type: {a.contact_type.value}")
    print(f"Location: {a.location}")
    print(f"Signal: {a.signal_strength:.1f}/10")
    print(f"Duration: {a.duration_minutes} minutes")
    print(f"Witnesses: {a.witness_count}")
    print(f"Message: '{a.message_received}'")
    print()


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")
    try:
        valid_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            contact_type=ContactType.RADIO,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
        )
        print_contact_info(valid_contact)

    except ValidationError as e:
        print(e)
    print("========================================")
    print("Expected validation error:")
    try:
        invalid_contact = AlienContact(
            contact_id="AC002",
            timestamp=datetime.now(),
            location="Sector 7G",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.0,
            duration_minutes=30,
            witness_count=1,
        )
        print_contact_info(invalid_contact)
    except (ValidationError) as e:
        for error in e.errors():
            print(f"{error['msg']}")


if __name__ == "__main__":
    main()
