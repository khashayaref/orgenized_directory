import shutil
from pathlib import Path

from src.data import DATA_DIR
from src.utils.io import read_json
from loguru import logger


class OrgenizedFiles:
    def __init__(self, path_files: str):
        """clean the directory by moving a file to its related directory

        :param path_files: the path of the directrory
        """
        self.path_files = Path(path_files)

        if not self.path_files.exists():
            raise FileNotFoundError(f'{self.path_files} does not exist')
        
        extention_files = read_json(DATA_DIR / 'file_extention.json')
        extentions = {}
        for key, value in extention_files.items():
            for item in extention_files[key]:
                extentions[item] = key
        self._file_extentions = extentions

    def __call__(self):
        """orgenizing files by moving them to their directories
        """
        extentions = []
        for file in self.path_files.iterdir():
            
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
            DIST_DIR = self.path_files / self._file_extentions[file.suffix]
            DIST_DIR.mkdir(exist_ok=True)
            shutil.move(str(file), str(DIST_DIR))
            logger.info(f'Moving {file} to {DIST_DIR}')
            
if __name__ == "__main__":
    orgenize_file = OrgenizedFiles('/home/khashayar/Downloads')
    orgenize_file()
    print('done')
        
        