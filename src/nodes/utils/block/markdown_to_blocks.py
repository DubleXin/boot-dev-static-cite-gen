def markdown_to_blocks(markdown: str) -> list[str]:
    splitted = list(
        filter(
            lambda s: s is not None and len(s) > 0,
            [item.strip() for item in markdown.split("\n\n")],
        )
    )
    if not splitted:
        return [markdown]
    return splitted
