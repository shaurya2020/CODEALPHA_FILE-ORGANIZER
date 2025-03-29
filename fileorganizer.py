import os
import shutil

# Define file type categories and target folders
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Music': ['.mp3', '.wav', '.aac', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Executables': ['.exe', '.msi', '.bat'],
    'Code': ['.py', '.java', '.cpp', '.html', '.css', '.js']
}

# Set folder path (change to your desired folder)
SOURCE_FOLDER = r'C:\Users\YourUsername\Downloads'  # Change to your target folder

def create_folders():
    for folder in FILE_TYPES.keys():
        folder_path = os.path.join(SOURCE_FOLDER, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def organize_files():
    files = os.listdir(SOURCE_FOLDER)
    for file in files:
        file_path = os.path.join(SOURCE_FOLDER, file)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1].lower()
            moved = False
            for folder, extensions in FILE_TYPES.items():
                if file_extension in extensions:
                    target_folder = os.path.join(SOURCE_FOLDER, folder)
                    shutil.move(file_path, target_folder)
                    print(f"Moved: {file} ➔ {folder}")
                    moved = True
                    break
            if not moved:
                # Create "Others" folder for unknown file types
                others_folder = os.path.join(SOURCE_FOLDER, 'Others')
                if not os.path.exists(others_folder):
                    os.makedirs(others_folder)
                shutil.move(file_path, others_folder)
                print(f"Moved: {file} ➔ Others")

def main():
    print("🛠️ Starting File Organizer...")
    create_folders()
    organize_files()
    print("✅ File organization complete!")

if __name__ == "__main__":
    main()
