import os
import shutil
from os.path import exists, isfile, join


def copy_static(parent_dir: str, public_dir: str = "public"):
    if not exists(f"{parent_dir}"):
        raise ValueError(
            f"Tnvalid parent directory. Path does not exists. Actual argument is: {parent_dir}"
        )
    path_to_static = join(parent_dir, "static")
    path_to_target = join(parent_dir, public_dir)
    if not exists(path_to_static):
        raise ValueError(
            f'The "static" directory is missing from the parent directory (the "parent_dir" argument). '
            f"Path being checked: {path_to_static}.\n File tree in {parent_dir}: {os.listdir(parent_dir)}"
        )
    os.mkdir(path_to_target)
    _copy_rec("", path_to_static, path_to_target)


def _copy_rec(current_path: str, source_root: str, target_root: str) -> None:
    if not exists(join(source_root, current_path)):
        print(f"{join(source_root, current_path)} does not exists")
        return

    source_path = join(
        source_root,
        current_path,
    )
    for dir in os.listdir(source_path):
        if isfile(join(source_path, dir)):
            shutil.copy(
                join(source_root, current_path, dir),
                join(target_root, current_path, dir),
            )
            continue
        os.mkdir(join(target_root, current_path, dir))
        _copy_rec(join(current_path, dir), source_root, target_root)
