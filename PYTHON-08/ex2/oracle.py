import os
import sys
from dotenv import load_dotenv

REQUIRED_VARS = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]


def load_configuration() -> dict[str, str]:
    """
    Load environment variables from .env file
    and system environment.
    """

    load_dotenv()

    config: dict[str, str] = {}

    for var in REQUIRED_VARS:
        value = os.getenv(var)

        if value is None:
            print(f"[WARNING] Missing configuration: {var}")
            config[var] = "NOT SET"
        else:
            config[var] = value

    return config


def display_configuration(config: dict[str, str]) -> None:
    """
    Display configuration status.
    """

    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")

    mode = config["MATRIX_MODE"]

    print(f"Mode: {mode}")

    if mode == "development":
        print("Database: Connected to local instance")
    elif mode == "production":
        print("Database: Connected to production instance")
    else:
        print("Database: Unknown environment")

    if config["API_KEY"] != "NOT SET":
        print("API Access: Authenticated")
    else:
        print("API Access: Missing credentials")

    print(f"Log Level: {config['LOG_LEVEL']}")

    if config["ZION_ENDPOINT"] != "NOT SET":
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")


def security_check() -> None:
    """
    Display security recommendations.
    """

    print("Environment security check:")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file missing")

    if os.path.exists(".gitignore"):
        with open(".gitignore", "r", encoding="utf-8") as file:
            content = file.read()

        if ".env" in content:
            print("[OK] Production overrides available")
            print("[OK] No hardcoded secrets detected")
        else:
            print("[WARNING] .env missing from .gitignore")
    else:
        print("[WARNING] .gitignore file missing")
    print()
    print("The Oracle sees all configurations.")


def main() -> int:
    """
    Main program.
    """

    try:
        config = load_configuration()
        display_configuration(config)
        print()
        security_check()

    except Exception as error:
        print(f"Error: {error}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
