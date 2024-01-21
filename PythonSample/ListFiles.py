import os
import logging
from typing import List

logging.basicConfig(level=logging.INFO)


def find(path: str, filename: str) -> List[str]:
    files = []
    try:
        for d in os.listdir(path):
            full_path = os.path.join(path, d)
            if os.path.isdir(full_path):
                files.extend(find(full_path, filename))
            elif os.path.isfile(full_path) and d == filename:
                print(f"Found file: {full_path}")
                files.append(full_path)
    except PermissionError as pe:
        logging.error(f"{pe}")
    except FileNotFoundError as fnfe:
        logging.error(f"{fnfe}")
    except IsADirectoryError as iade:
        logging.error(f"Expected {path} to be a file but it's a directory: {iade}")
    return files


def main():
    directory = input("Enter a directory to search in: ")
    filename = input("Enter a file to search for: ")
    files_found = find(directory, filename)
    print(files_found)


if __name__ == "__main__":
    main()
