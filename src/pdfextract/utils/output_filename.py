from pathlib import Path


def generate_unique_filename(base_filename="output") -> Path:
    """Generates a unique filename that doesn't conflict with existing files."""
    counter = 0
    while True:
        filename = Path(f"{base_filename}_{counter}.pdf")
        if not filename.exists():
            break
        counter += 1
    return filename
