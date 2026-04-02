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


def summary_output(source_folder):
    videos = 0
    images = 0
    documents = 0
    audio = 0
    compressed = 0
    code = 0
    others = 0

    for file in os.listdir(source_folder):
        old_path = os.path.join(source_folder, file)

        if os.path.isfile(old_path):

            if file.lower().endswith((".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv")):
                videos += 1

            elif file.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp")):
                images += 1

            elif file.lower().endswith((".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx")):
                documents += 1

            elif file.lower().endswith((".mp3", ".wav", ".aac", ".flac", ".ogg")):
                audio += 1

            elif file.lower().endswith((".zip", ".rar", ".7z", ".tar", ".gz")):
                compressed += 1

            elif file.lower().endswith((".py", ".java", ".cpp", ".c", ".js", ".html", ".css", ".json")):
                code += 1

            else:
                others += 1

    # Final summary output
    print(f"Moved {images} image files")
    print(f"Moved {videos} video files")
    print(f"Moved {documents} document files")
    print(f"Moved {audio} audio files")
    print(f"Moved {compressed} compressed files")
    print(f"Moved {code} code files")
    print(f"Moved {others} other files")
    total = videos + images + documents + audio + compressed + code + others
    print(f"\nTotal files processed: {total}")


def main():
    while True:
        source_folder = input("Enter your source folder path: ")

        if not os.path.isdir(source_folder):
            print("The source folder path does not exist. Please try again.")
            continue

        if len(os.listdir(source_folder)) == 0:
            print("The folder is empty! Please choose a folder with files.")
            continue

        break  

    
    while True:
        destination_check = input("Do you want to add a destination folder? (yes/no): ").lower()

        if destination_check == "yes" or destination_check == "y":
            destination_folder = input("Enter your destination folder path: ")
            if os.path.isdir(destination_folder):
               break
            else:
               print("The destination folder path does not exist. Please try again.")
            

        elif destination_check == "no" or destination_check == "n":
            destination_folder = source_folder
            break

        else:
            print("Enter only yes, no, y, or n!")

    make_subfolders(destination_folder)
    summary_output(source_folder)
    folder_scan(source_folder, destination_folder)
    


if __name__ == "__main__":
    main()