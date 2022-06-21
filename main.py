from stackoverflow_api import *
from ya_disk_api import *


def main():
    while True:
        user_choose = input("Введите команду:")
        if user_choose == "y":
            token = input("Введите токен:")
            yd = YaUploader(token)
            file_path = input("Введите деректорию для расположения файла в хранилище:")
            filename = input("Введите путь к файлу на диске:")
            yd.upload_file(file_path=file_path, filename=filename)
        if user_choose == "s":
            tag = input("Введите необходимый тег:")
            get_questions(tag)


if __name__ == "__main__":
    main()
