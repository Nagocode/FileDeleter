# Import required libraries
import os
import time

# Dictionary with folders to process
folders = {
    "folder_1": r"C:\example\path\folder1",
    "folder_2": r"C:\example\path\folder2",
    "folder_3": r"C:\example\path\folder3"
}

# Get current time in seconds
now = time.time()

# Time threshold in seconds (2 days)
threshold = 2 * 86400  # 2 days

# Iterate through each folder
for name, path in folders.items():
    print(f"\nProcessing {name}: {path}")
    # Loop through the files in the folder
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            last_modified = os.path.getmtime(file_path)
            # Check if the file is older than the threshold
            if now - last_modified > threshold:
                try:
                    os.remove(file_path)  # Delete the file
                    print(f"Deleted file: {file}")
                except Exception as e:
                    print(f"Error deleting {file}: {e}")
