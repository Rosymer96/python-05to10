import sys
import os
import site


def is_env() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:
    env = is_env()
    current_python = sys.executable
    if env:
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {current_python}")
        env_name = os.path.basename(sys.prefix)
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {sys.prefix}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print()
        print("Package installation path:")
        for sitepackage in site.getsitepackages():
            print(sitepackage)
    else:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {current_python}")
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")

        if os.name == "posix":
            print("source matrix_env/bin/activate\n")
        else:
            print(r"matrix_env\Scripts\activate\n")
        print("Then run this program again.")


if __name__ == "__main__":
    main()
