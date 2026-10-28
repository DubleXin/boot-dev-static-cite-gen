import os
from os.path import exists, isfile, join

from src.view_builder.page_generator.generate_page import generate_page


def generate_pages_recursive(
    dir_path_content: str, template_path: str, dest_dir_path: str, basepath="/"
) -> None:
    if not exists(f"{template_path}"):
        raise ValueError(
            f"Tnvalid path of the template file. Path does not exists. Actual argument is: {template_path}"
        )
    if not exists(f"{dir_path_content}"):
        raise ValueError(
            f"Tnvalid path of content. Path does not exists. Actual argument is: {dir_path_content}"
        )
    for v in os.listdir(dir_path_content):
        if v[-3:] == ".md" and isfile(join(dir_path_content, v)):
            generate_page(
                join(dir_path_content, v),
                template_path,
                join(dest_dir_path, f"{v[:-3]}.html"),
                basepath,
            )
            continue
        generate_pages_recursive(
            join(dir_path_content, v), template_path, join(dest_dir_path, v), basepath
        )
