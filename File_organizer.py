import os
import shutil
from datetime import datetime


def folder_scan(source_folder, destination_folder, custom_folders, sort):
    counts = {
        "videos": 0,
        "images": 0,
        "documents": 0,
        "audio": 0,
        "compressed": 0,
        "code": 0,
        "others": 0
    }

    # Add custom folders to counts
    for key in custom_folders.keys():
        counts[key] = 0

    for file in os.listdir(source_folder):
        old_path = os.path.join(source_folder, file)

        if not os.path.isfile(old_path):
            continue

        folder_name = "others"
        filetype = "others"
        matched = False

        # Check custom categories
        for custom_folder, file_ext in custom_folders.items():
            extensions = tuple(ext.strip() for ext in file_ext.split(","))

            if file.lower().endswith(extensions):
                folder_name = custom_folder
                filetype = custom_folder
                matched = True
                break

        # Default categories
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

        # Date sorting
        if sort:
            timestamp = os.path.getmtime(old_path)
            year = str(datetime.fromtimestamp(timestamp).year)

            folder_path = os.path.join(folder_path, year)
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
            print(f"❌ Failed to move: {file} | Error: {e}")

    # Summary
    print("\n===== FILE SUMMARY =====")

    for key, value in counts.items():
        if value > 0:
            print(f"{key.capitalize():12} : {value}")

    print("------------------------")
    print(f"Total files : {sum(counts.values())}")
    print("\n✔ Files organized successfully!")
    print(f"📁 Saved in: {destination_folder}")
    print("Thank you for using File Organizer 🚀")


def make_subfolders(destination_folder, custom_folders):
    folders = [
        "videos",
        "images",
        "documents",
        "audio",
        "compressed",
        "code",
        "others"
    ]

    folders.extend(custom_folders.keys())

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
            print("\n1. Organize by type")
            print("   → Files will be sorted into folders like:")
            print("     Images/")
            print("     Videos/")
            print("     Documents/")
 
            print("\n2. Organize by type + date")
            print("   → Files will be sorted by type AND year like:")
            print("     Images/2024/")
            print("     Images/2025/")
            print("     Videos/2023/")
 
            print("\nExample:")
            print("Option 1:")
            print("  Images/")
            print("  Videos/")
 
            print("\nOption 2:")
            print("  Images/2024/")
            print("  Videos/2023/")
 
            print("\nChoose based on your preference.\n")

            choose = input("Enter your choice (1-2): ")

            if choose == "1":
                sort = False
            elif choose == "2":
                sort = True
            else:
                print("Invalid choice! Please enter 1 or 2.")
                continue

            print("\nStarting file organization...\n")

            # Source folder
            while True:
                source_folder = input("Enter source folder path: ")

                if not os.path.isdir(source_folder):
                    print("❌ Source folder does not exist.")
                    continue

                if not os.listdir(source_folder):
                    print("⚠ Folder is empty.")
                    continue

                break

            # Destination folder
            while True:
                destination_check = input("Use a separate destination folder? (yes/no): ").lower()

                if destination_check in ["yes", "y"]:
                    destination_folder = input("Enter destination folder path: ")

                    if os.path.isdir(destination_folder):
                        break
                    else:
                        print("❌ Destination folder does not exist.")

                elif destination_check in ["no", "n"]:
                    destination_folder = source_folder
                    break

                else:
                    print("Enter only yes or no.")

            # Custom folders
            custom_folders = {}

            while True:
                custom_folder_check = input(
                    "Do you want to add custom categories? (yes/no): "
                ).lower()

                if custom_folder_check in ["yes", "y"]:
                    name = input("Enter category name: ")
                    ext = input("Enter extensions (comma separated): ")

                    custom_folders[name] = ext

                    more = input("Add another category? (yes/no): ").lower()

                    if more in ["no", "n"]:
                        break

                elif custom_folder_check in ["no", "n"]:
                    break

                else:
                    print("Enter only yes or no.")

            make_subfolders(destination_folder, custom_folders)
            folder_scan(source_folder, destination_folder, custom_folders, sort)

        else:
            print("Invalid choice! Please enter 1 or 2.")


if __name__ == "__main__":
    main()