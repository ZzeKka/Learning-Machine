"""
Shebang for linux and bat file for Windows
"""
#!/usr/bin/env python3


import nbformat
from pathlib import Path

course_sections_directories = ["Machine Learning Specialization","python scrits"]


def format_ipynb_markdown(filename):
    ...

def main() -> None:
    current = Path('.').resolve().parent # Project root folder
    format_ipynb_markdown_full_dir(current)

def format_ipynb_markdown_full_dir(dir: Path) -> None:
    current = Path('.').resolve().parent # Project root folder
    print(f"Current path is: {current}")
    for course_section_directory in course_sections_directories:
        if Path(current / course_section_directory).exists():
            # Call markdown changer function
            ...

def format_ipynb_markdown_file(filename: str) -> None:
    ...
        

if __name__ == "__main__":
    main()

