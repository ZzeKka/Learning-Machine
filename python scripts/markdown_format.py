"""
Shebang for linux and bat file for Windows
"""
#!/usr/bin/env python3

from pathlib import Path
import nbformat
import re


hexa_colors_keywords_c1 = {
    r'supervised learning': '#000080',
    r'unsupervised learning': '#7B68EE',
    r'inputs?': '#98FB98',
    r'outputs?': '#FF0000',
}


course_sections_directories = ["Supervided Learning"]

def main() -> None:
    root = Path('.').resolve().parent # Project root folder
    format_ipynb_markdown_file(root / 'Machine Learning Specialization' / 'test.ipynb')

def format_ipynb_markdown_full_dir(dir: Path) -> None:
    current = Path('.').resolve().parent # Project root folder
    for course_section_directory in course_sections_directories:
        if Path(current / course_section_directory).exists():
            format_ipynb_markdown_file()
        else:
            print(f"Directory of name: '{course_section_directory}' doens't exist")


# FINISH THIS FUNCTION TO CHANGE CERTAIN KEYWORDS TO A CERTAIN COLOR AND BOLDNESS
def format_ipynb_markdown_file(file_path: Path) -> None:
    old_notebook = nbformat.read(file_path , as_version=4)
    new_notebook = nbformat.read(file_path , as_version=4)
    for old_cell, new_cell in zip(old_notebook.cells, new_notebook.cells):
        if new_cell.cell_type == "markdown":
            new_cell.source = format_ipynb_markdown_cell(old_cell.source)
    with open(file_path, 'w') as replace_notebook:
        nbformat.write(new_notebook, replace_notebook)

# Formats cells to give keyword colors if it already has a color it overwrites the current one
def format_ipynb_markdown_cell(old_cell_source):
    text = old_cell_source
    for keyword, color in hexa_colors_keywords_c1.items():
        # *? used to add lazy behaviour instead of greedy and not overshooting the ending of the pattern
        pattern = re.compile(
            rf'<span style="color:[a-zA-Z0-9#]*?">{keyword}<\/span>'
            rf'|\b[^\s\w]?{keyword}\b[^\s\w]?\b',
            flags=re.IGNORECASE
        )

        def replacer(match) -> str:
            matched_text = match.group(0)
            # If it is already inside a span, replace the color
            if matched_text.startswith('<span'):
                # Replace color inside span tag with the new color
                return re.sub(r'color:[a-zA-Z0-9#]*', f'color:{color}', matched_text)
            else:
                # Wrap plain word in new span with color
                return f'<span style="color:{color}">{matched_text}</span>'

        text = re.sub(pattern, replacer, text)
    return text

if __name__ == "__main__":
    main()

