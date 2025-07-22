# file_organizer.py

import os
import shutil


import os
import shutil

def organize_files(folder_path):
    try:
        files = os.listdir(folder_path)
        for file in files:
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                ext = os.path.splitext(file)[1].lower()

                if ext in ['.jpg', '.png']:
                    dest_folder = os.path.join(folder_path, 'Images')
                elif ext in ['.docx', '.pdf']:
                    dest_folder = os.path.join(folder_path, 'Documents')
                else:
                    dest_folder = os.path.join(folder_path, 'Others')

                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)

                shutil.move(file_path, os.path.join(dest_folder, file))

        print("Files organized successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    path = input("Enter the full path to the folder you want to organize: ")
    organize_files(path)
