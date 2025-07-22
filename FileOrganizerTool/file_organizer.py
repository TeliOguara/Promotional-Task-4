import os
import shutil

def organize_files(folder_path):
    # Define target folders and file extensions
    file_types = {
        "Images": [".jpg", ".jpeg", ".png"],
        "Documents": [".pdf", ".docx", ".txt"]
    }

    # Create subfolders if they don't exist
    for folder in file_types:
        target_dir = os.path.join(folder_path, folder)
        os.makedirs(target_dir, exist_ok=True)

    # Loop through files and move them
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename.lower())
            for folder, extensions in file_types.items():
                if ext in extensions:
                    shutil.move(file_path, os.path.join(folder_path, folder, filename))
                    print(f"Moved {filename} → {folder}/")
                    break

# Ask user for folder path
folder_path = input("Enter the full path to the folder you want to organize: ").strip()

if os.path.isdir(folder_path):
    organize_files(folder_path)
    print("✔️ Files organized successfully.")
else:
    print("❌ The specified folder does not exist.")
