# ==========================================
# Task Automation - File Renamer
# CodeAlpha Python Internship Project
# Author: Afrin
# ==========================================

import os


# Function to rename text files
def rename_files():
    print("\n📂 FILE RENAMER AUTOMATION")
    print("-" * 40)

    # Get folder path from user
    folder_path = input("Enter the folder path: ")

    # Check whether folder exists
    if not os.path.exists(folder_path):
        print("❌ Folder does not exist.")
        return

    # Get all files from the folder
    files = os.listdir(folder_path)

    # Store only .txt files
    text_files = []

    for file in files:
        if file.endswith(".txt"):
            text_files.append(file)

    # Check if there are text files
    if len(text_files) == 0:
        print("❌ No .txt files found in this folder.")
        return

    print("\n📄 Text Files Found:")
    for file in text_files:
        print(file)

    print("\n🔄 Renaming Files...")

    count = 1

    # Rename files
    for file in text_files:
        old_path = os.path.join(folder_path, file)

        new_name = f"file_{count}.txt"
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)

        print(f"✅ {file}  ➜  {new_name}")

        count += 1

    print("\n🎉 File renaming completed successfully!")
    print(f"Total files renamed: {count - 1}")


# Main Program
print("======================================")
print("      TASK AUTOMATION PROJECT")
print("======================================")

while True:
    rename_files()

    choice = input(
        "\nDo you want to automate another folder? (yes/no): "
    ).lower()

    if choice != "yes":
        break

print("\nThank you for using Task Automation!")