import os
import shutil


def folder_scan(source_folder, destination_folder,custom_folders):
    counts = {
        "videos": 0,
        "images": 0,
        "documents": 0,
        "audio": 0,
        "compressed": 0,
        "code": 0,
        "others": 0
    }
    for keys in custom_folders.keys():
             counts[keys]=0
    for file in os.listdir(source_folder):
        old_path = os.path.join(source_folder, file)


        if not os.path.isfile(old_path):
            continue

        folder_name = "others"
        filetype = "others"
        matched=False
        
        for custom_folder , file_ext in custom_folders.items():
            file_ext_split=tuple(ext.strip() for ext in file_ext.split(","))
            if file.lower().endswith(file_ext_split):
               matched=True
               folder_name=custom_folder
               filetype=custom_folder
               break
        if not matched:

            if file.lower().endswith((".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv")):
                    folder_name = "videos"
                    filetype = "videos"

            elif file.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp")):
                    folder_name = "images"
                    filetype = "images"

            elif file.lower().endswith((".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx")):
                    folder_name = "documents"
                    filetype = "documents"

            elif file.lower().endswith((".mp3", ".wav", ".aac", ".flac", ".ogg")):
                    folder_name = "audio"
                    filetype = "audio"

            elif file.lower().endswith((".zip", ".rar", ".7z", ".tar", ".gz")):
                    folder_name = "compressed"
                    filetype = "compressed"

            elif file.lower().endswith((".py", ".java", ".cpp", ".c", ".js", ".html", ".css", ".json")):
                    folder_name = "code"
                    filetype = "code"

        folder_path = os.path.join(destination_folder, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        new_path = os.path.join(folder_path, file)

        name, ext = os.path.splitext(file)
        i = 1
        while os.path.exists(new_path):
                new_name = f"{name}({i}){ext}"
                new_path = os.path.join(folder_path, new_name)
                i += 1

        try:
                shutil.move(old_path, new_path)
                counts[filetype] += 1
        except Exception as e:
            print(f"Failed to move: {file} | Error: {e}")
    print("\n===== File Summary =====")
    for key , value in counts.items():  
      print(f"{key.capitalize():12} : {value}")
    print("------------------------")
    print(f"Total files: {sum(counts.values())}")   
    print("✔ Files organized successfully")
    print("Thanks for using File Organizer")
   


def make_subfolders(destination_folder,custom_folders=None):
    folders = [
        "videos",
        "images",
        "documents",
        "audio",
        "compressed",
        "code",
        "others"
    ]
    for custom_folder , file_ext in custom_folders.items():
      folders.append(custom_folder)
    for folder in folders:
        os.makedirs(os.path.join(destination_folder, folder), exist_ok=True)


def main():
    print("\n" + "=" * 30)
    print("FILE ORGANIZER".center(30))
    print("=" * 30)
    print("1. Organize Files")
    print("2. Exit")
    print("=" * 30)

    while True:
        choice = input("Enter your choice (1-2): ")

        if choice == "2":
            print("Exiting program...")
            break

        elif choice == "1":
            print("Starting file organization...\n")

            while True:
                source_folder = input("Enter your source folder path: ")

                if not os.path.isdir(source_folder):
                    print("The source folder does not exist. Please try again.")
                    continue

                if len(os.listdir(source_folder)) == 0:
                    print("The folder is empty! Please choose a folder with files.")
                    continue

                break

            while True:
                destination_check = input(
                    "Do you want to choose a destination folder? (yes/no): "
                ).lower()

                if destination_check in ["yes", "y"]:
                    destination_folder = input("Enter destination folder path: ")

                    if os.path.isdir(destination_folder):
                        break
                    else:
                        print("Destination folder does not exist. Try again.")

                elif destination_check in ["no", "n"]:
                    destination_folder = source_folder
                    break

                else:
                    print("Please enter only yes, no, y, or n.")
            while True:
                custom_folder_check= input(
                    "Do you want to add custom subfolder? for specific file types (yes/no): "
                ).lower()
                custom_folders={}
                if custom_folder_check in ["yes", "y"]:
                    custom_folder = input("Enter subfolder  name: ")
                    file_ext=input("Enter the file extension:")
                    custom_folders[custom_folder] = file_ext
                    check=input("Enter yes to add one more subfolder or no to not add:")
                    if check in ["no", "n"]:
                        break
                    elif check in  ["yes", "y"]:
                        continue
                    else:
                      print("Please enter only yes, no, y, or n.")
                elif custom_folder_check in ["no", "n"]:
                    break
                else:
                    print("Please enter only yes, no, y, or n.")
                           
            make_subfolders(destination_folder,custom_folders)
            folder_scan(source_folder, destination_folder,custom_folders)

        else:
            print("Invalid choice! Please enter 1 or 2.")


if __name__ == "__main__":
    main()