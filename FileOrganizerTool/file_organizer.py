import os
import shutil

# Ask user for folder path
folder_path = input("Enter the full path to the folder you want to organize: ")

# Create target directories if they don't exist
images_dir = os.path.join(folder_path, "Images")
docs_dir = os.path.join(folder_path, "Documents")

os.makedirs(images_dir, exist_ok=True)
os.makedirs(docs_dir, exist_ok=True)

# Organize files
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        if filename.lower().endswith((".jpg", ".png")):
            shutil.move(file_path, os.path.join(images_dir, filename))
        elif filename.lower().endswith((".docx", ".pdf")):
            shutil.move(file_path, os.path.join(docs_dir, filename))

print("Organization complete.")
