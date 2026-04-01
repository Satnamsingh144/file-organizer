import os
import shutil


def folder_scan(source_folder, destination_folder):
    for file in os.listdir(source_folder):
        old_path = os.path.join(source_folder, file)

        if os.path.isfile(old_path):

            if file.lower().endswith((".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv")):
                folder_name = "videos"

            elif file.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp")):
                folder_name = "images"

            elif file.lower().endswith((".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx")):
                folder_name = "documents"

            elif file.lower().endswith((".mp3", ".wav", ".aac", ".flac", ".ogg")):
                folder_name = "audio"

            elif file.lower().endswith((".zip", ".rar", ".7z", ".tar", ".gz")):
                folder_name = "compressed"

            elif file.lower().endswith((".py", ".java", ".cpp", ".c", ".js", ".html", ".css", ".json")):
                folder_name = "code"

            else:
                folder_name = "others"

            folder_path = os.path.join(destination_folder, folder_name)
            new_path = os.path.join(folder_path, file)

            name, ext = os.path.splitext(file)
            i = 1

            while os.path.exists(new_path):
                new_name = f"{name}({i}){ext}"
                new_path = os.path.join(folder_path, new_name)
                i += 1

            shutil.move(old_path, new_path)


def make_subfolders(destination_folder):
    folders = [
        "videos",
        "images",
        "documents",
        "audio",
        "compressed",
        "code",
        "others"
    ]

    for folder in folders:
        os.makedirs(os.path.join(destination_folder, folder), exist_ok=True)


def main():
    source_folder = input("Enter your source folder path: ")
    
    while True:
        destination_check = input("Do you want to add a destination folder? (yes/no): ").lower()

        if destination_check == "yes" or destination_check == "y":
            destination_folder = input("Enter your destination folder path: ")
            break

        elif destination_check == "no" or destination_check == "n":
            destination_folder = source_folder
            break

        else:
            print("Enter only yes, no, y, or n!")

    make_subfolders(destination_folder)
    folder_scan(source_folder, destination_folder)


if __name__ == "__main__":
    main()