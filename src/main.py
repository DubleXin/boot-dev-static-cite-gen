from src.bcolors import BColor as bc
from src.view_builder.copy_static import copy_static
from src.view_builder.delete_public import delete_public

root_path = "."

try:
    print(f"\n{bc.OKCYAN}Deleting public directory...{bc.ENDC}\n")
    delete_public(root_path)
    print(
        f"\n{bc.OKCYAN}Copying static directory to new public directory...{bc.ENDC}\n"
    )
    copy_static(root_path)
except ValueError as err:
    print(
        f"{bc.WARNING}Failed to copy static directory to newly created public directory{bc.ENDC}\n{bc.FAIL}Actual error: {err}{bc.ENDC}"
    )
