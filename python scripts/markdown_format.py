"""
Shebang for linux and bat file for Windows
"""
#!/usr/bin/env python3

from pathlib import Path
import nbformat
import re


hexa_colors_keywords_c1 = {
    r'supervised learning': '#000080',
    r'unsupervised learning': "#EE68A2",
    r'regression?': "#AD98FB",
    r'classification?': "#8800FF",
    r'inputs?': '#98FB98',
    r'outputs?': '#FF0000',
    
}

course = ['Machine Learning Specialization']

# Main function, calls the functions the modify the markdown
def main() -> None:
    root = Path('.').resolve().parent 
    # Modify all the jupyter notebook markdown in the directory
    format_ipynb_markdown_full_dir(root / 'Machine Learning Specialization') # Hardcoded, but easely changed with a for loop

# Checks if the path is a jupyter notebook
def format_ipynb_markdown_full_dir(course_path: Path) -> None:
    for course_section_path in course_path.iterdir():
        if course_section_path.is_file() and course_section_path.suffix == '.ipynb':
            detec_markdown_cells(course_path / course_section_path)

# Checks for Markdowns cells and then calls the function that changes those cells
def detec_markdown_cells(file_path: Path) -> None:
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
                return re.sub(r'color:[#a-zA-Z0-9]*?">\*{0,2}', f'color:{color}">**', re.sub(r'\*{0,2}\s*</span>', '**</span>',matched_text))
            else:
                # Wrap plain word in new span with color
                return f'<span style="color:{color}">**{matched_text}**</span>'
        text = re.sub(pattern, replacer, text)
    return text

if __name__ == "__main__":
    main()

