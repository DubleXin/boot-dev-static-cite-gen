import os
from os.path import dirname, exists

from src.bcolors import BColor
from src.nodes.markdown_to_html_node import markdown_to_html_node
from src.view_builder.utils.extract_title import extract_title


def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print(
        f"Generating page from {BColor.BOLD}{from_path}{BColor.ENDC} to {BColor.BOLD}{dest_path}{BColor.ENDC} using {BColor.BOLD}{template_path}{BColor.ENDC}"
    )
    if not exists(f"{from_path}"):
        raise ValueError(
            f"Tnvalid path of the markdown file. Path does not exists. Actual argument is: {from_path}"
        )

    markdown_content: str = ""
    template_content: str = ""
    with open(from_path) as f:
        markdown_content = f.read()
    with open(template_path) as f:
        template_content = f.read()

    html_content = markdown_to_html_node(markdown_content).to_html()
    document_title = extract_title(markdown_content)

    title_splited = template_content.split("{{ Title }}", 1)
    template_content = "".join([title_splited[0], document_title, title_splited[1]])
    content_splited = template_content.split("{{ Content }}", 1)

    document = "".join([content_splited[0], html_content, content_splited[1]])

    os.makedirs(dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(document)
