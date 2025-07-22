import os
import shutil

def organize_files(folder_path):
    file_types = {
        "Images": [".jpg", ".jpeg", ".png"],
        "Documents": [".pdf", ".docx", ".txt"]
    }

    for folder in file_types:
        target_dir = os.path.join(folder_path, folder)
        os.makedirs(target_dir, exist_ok=True)

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename.lower())
            for folder, extensions in file_types.items():
                if ext in extensions:
                    try:
                        shutil.move(file_path, os.path.join(folder_path, folder, filename))
                        print(f"Moved {filename} → {folder}/")
                    except PermissionError:
                        print(f"Permission denied: {filename}")
                    except Exception as e:
                        print(f"Error moving {filename}: {e}")
                    break

# Main execution
folder_path = input("Enter the full path to the folder you want to organize: ").strip()

if not os.path.isdir(folder_path):
    print("The specified folder does not exist.")
else:
    try:
        organize_files(folder_path)
        print("All supported files have been organized.")
    except Exception as e:
        print(f"An error occurred during organization: {e}")
