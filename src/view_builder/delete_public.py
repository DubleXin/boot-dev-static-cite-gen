import os
import shutil


def delete_public(parent_dir: str):
    if not os.path.exists(f"{parent_dir}"):
        raise ValueError(
            f"Tnvalid parent directory. Path does not exists. Actual argument is: {parent_dir}"
        )
    target_path = os.path.join(parent_dir, "public")
    if not os.path.exists(f"{target_path}"):
        raise ValueError(
            f'The "public" directory is missing from the parent directory (the "parent_dir" argument). '
            f"Path being checked: {target_path}.\n File tree in {parent_dir}: {os.listdir(parent_dir)}"
        )
    shutil.rmtree(target_path)
