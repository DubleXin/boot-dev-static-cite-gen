import os
import shutil
from os.path import exists, join


def delete_public_directory(parent_dir: str, public_dir: str = "public"):
    if not exists(f"{parent_dir}"):
        raise ValueError(
            f"Tnvalid parent directory. Path does not exists. Actual argument is: {parent_dir}"
        )
    target_path = join(parent_dir, public_dir)
    if not exists(f"{target_path}"):
        raise ValueError(
            f'The "{public_dir}" directory is missing from the parent directory (the "parent_dir" argument). '
            f"Path being checked: {target_path}.\n File tree in {parent_dir}: {os.listdir(parent_dir)}"
        )
    shutil.rmtree(target_path)
