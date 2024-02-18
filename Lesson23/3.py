import os
from argparse import ArgumentParser
from typing import Dict


def get_statistics(root_folder: str) -> Dict[str, int]:
    """Calculates the number of folders and files in a given root directory.

    Args:
        root_folder (str): The path to the root directory to analyze.

    Returns:
        Dict[str, int]: A dictionary containing the statistics, with keys 'folders' and 'files'.
    """
    folders_count, files_count = 0, 0
    for root, folders, files in os.walk(root_folder):
        folders_count += len(folders)
        files_count += len(files)

    return {'folders': folders_count, 'files': files_count}


def format_statistics(stat_info: Dict[str, int]) -> str:
    """Formats the statistics into a human-readable string.

    Args:
        stat_info (Dict[str, int]): The statistics dictionary.

    Returns:
        str: The formatted statistics string.
    """
    return f'Количество папок: {stat_info["folders"]}\n' \
           f'Количество файлов: {stat_info["files"]}'


def main():
    parser = ArgumentParser(
        prog="File OS Statistics",
        description="Утилита подсчета статистики файловой системы"
    )
    parser.add_argument("root", type=str, help="Путь к корневой папке анализа")
    args = parser.parse_args()

    root_folder = args.root

    try:
        stat_info = get_statistics(root_folder)
    except OSError as error:
        print(error)
    else:
        print(format_statistics(stat_info))


if __name__ == "__main__":
    main()
