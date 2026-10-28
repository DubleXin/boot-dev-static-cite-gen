import sys

from src.bcolors import BColor as bc
from src.view_builder.copy_static import copy_static
from src.view_builder.delete_public import delete_public_directory
from src.view_builder.page_generator.generate_pages_recursive import (
    generate_pages_recursive as gen,
)

root_path = "."
public_dir = "docs"
basepath = sys.argv[1] if len(sys.argv) - 1 >= 1 else "/"
print(
    f"{bc.HEADER}config:{bc.ENDC}\nroot path : {root_path}\tpublic dir: {public_dir}\tbase path: {basepath}"
)
try:
    print(f"\n{bc.OKCYAN}Deleting public directory...{bc.ENDC}\n")
    delete_public_directory(root_path, public_dir)
    print(
        f"\n{bc.OKCYAN}Copying static directory to new public directory...{bc.ENDC}\n"
    )
    copy_static(root_path, public_dir)
except ValueError as err:
    print(
        f"{bc.WARNING}Failed to copy static directory to newly created public directory{bc.ENDC}\n{bc.FAIL}Actual error: {err}{bc.ENDC}"
    )

try:
    gen("./content", "./template.html", "./docs", basepath)
except ValueError as err:
    print(
        f"{bc.WARNING}Failed to generate pages form content{bc.ENDC}\n{bc.FAIL}Actual error: {err}{bc.ENDC}"
    )
