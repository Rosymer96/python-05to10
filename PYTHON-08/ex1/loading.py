import importlib
import sys

PACKAGES = ["pandas", "numpy", "requests", "matplotlib"]


def check_installed(package: str) -> bool:
    try:
        descriptions = {
            "numpy": "Numerical computation ready",
            "pandas": "Data manipulation ready",
            "matplotlib": "Visualization ready",
            "requests": "Network access ready",
        }
        module = importlib.import_module(package)
        version = getattr(module, "__version__", "unknown")
        description = descriptions.get(package)
        print(f"[OK] {package} ({version}) - {description}")
        return True

    except ImportError:
        sys.stderr.write(f"[ERROR] '{package}' is not installed\n")
        return False


def check_dependencies() -> bool:
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    all_installed = True
    for package in PACKAGES:
        if not check_installed(package):
            all_installed = False
    return all_installed


def print_installed_help() -> None:
    print("\nInstall dependencies with:")
    print("pip install -r requirements.txt")
    print("\nOr with Poetry:")
    print("poetry install")


def analyze_data() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    matrix_data = np.random.randint(
        0,
        100,
        1000
    )
    print("\nAnalyzing Matrix data...")
    print(f"Processing {len(matrix_data)} data points...")
    dataframe = pd.DataFrame({"matrix_signal": matrix_data})
    mean_value = dataframe["matrix_signal"].mean()
    min_value = dataframe["matrix_signal"].min()
    max_value = dataframe["matrix_signal"].max()

    print("\nStatistics:")
    print(f"Mean: {mean_value:.2f}")
    print(f"Min: {min_value:.2f}")
    print(f"Max: {max_value:.2f}")

    print("\nGenerating visualization...")

    plt.figure(figsize=(10, 5))
    plt.plot(dataframe["matrix_signal"])
    plt.title("Matrix Signal Analysis")
    plt.xlabel("Data Point")
    plt.ylabel("Signal Strength")

    output_file = "matrix_analysis.png"

    plt.savefig(output_file)

    print("\nAnalysis complete!")
    print(f"Results saved to: {output_file}")


def main() -> None:
    try:
        if not check_dependencies():
            print_installed_help()
            sys.exit(1)
        analyze_data()

    except Exception as error:
        print(f"Unexpected error: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
