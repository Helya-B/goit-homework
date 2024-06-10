import argparse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor


def copy_file(file_path: Path, ext_folder: Path) -> None:
    try:
        with open(file_path, "rb") as src_file:
            with open(ext_folder / file_path.name, "wb") as dest_file:
                dest_file.write(src_file.read())
    except OSError as err:
        raise ValueError(f"Error copying {file_path}: {err}")


def process_folder(folder_path: Path) -> None:
    output = folder_path / "dist"
    output.mkdir(exist_ok=True, parents=True)

    with ThreadPoolExecutor() as executor:
        for file in folder_path.iterdir():
            if file.is_file():
                executor.submit(copy_file, file, output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sorting folder")
    parser.add_argument("--source", "-s", help="Source folder", required=True)
    args = vars(parser.parse_args())
    source = Path(args.get("source"))

    if source.is_dir():
        process_folder(source)
    else:
        raise ValueError("Invalid folder path.")
