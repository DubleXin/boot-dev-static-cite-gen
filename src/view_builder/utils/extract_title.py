def extract_title(markdown: str) -> str:
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()

    raise ValueError(
        'Markdown document does not contain an H1 heading starting with "# "'
    )
