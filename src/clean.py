import shutil
from pathlib import Path

from src.data import DATA_DIR
from src.utils.io import read_json
from loguru import logger
from typing import Union


class OrgenizedFiles:
    def __init__(self):
        """clean the directory by moving a file to its related directory
        """
        extention_files = read_json(DATA_DIR / 'file_extention.json')
        extentions = {}
        for key, value in extention_files.items():
            for item in extention_files[key]:
                extentions[item] = key
        self._file_extentions = extentions

    def __call__(self, path_files: Union[str, Path]):
        """orgenizing files by moving them to their directories

        :param path_files: the file directory
        """
        path_files = Path(path_files)

        if not path_files.exists():
            raise FileNotFoundError(f'{self.path_files} does not exist')
        extentions = []
        for file in path_files.iterdir():
            
            #ignore directories
            if file.is_dir():
                continue
            #ignore hidden files
            if file.name.startswith('.'):
                continue
                
            # get all file types
            extentions.append(file.suffix)
            if file.suffix not in self._file_extentions:
                continue
            DIST_DIR = path_files / self._file_extentions[file.suffix]
            DIST_DIR.mkdir(exist_ok=True)
            shutil.move(str(file), str(DIST_DIR))
            logger.info(f'Moving {file} to {DIST_DIR}')
            
if __name__ == "__main__":
    orgenize_file = OrgenizedFiles()
    orgenize_file('/home/khashayar/Downloads')
    print('done')
        