import os

def print_banner():
    banner = """
    ###############################################
    #          MASS FILE RENAMER SCRIPT           #
    #            Created by Python 2.7            #
    ###############################################
    """
    print(banner)
    
def mass_rename(directory, prefix, start_number=1, file_extension=None):
    try:
        files = os.listdir(directory)
        if not files:
            print("No files found in the directory.")
            return

        count = start_number
        for filename in files:
            old_path = os.path.join(directory, filename)
            if os.path.isdir(old_path):
                continue
            if file_extension and not filename.endswith(file_extension):
                continue

            new_filename = "{}_{}{}".format(
                prefix, str(count).zfill(3), os.path.splitext(filename)[1]
            ) ##u can change {}_{}{} zfill(3) to u can change {}_{} zfill(2)
            new_path = os.path.join(directory, new_filename)

            os.rename(old_path, new_path)
            print("Renamed: '{}' -> '{}'".format(filename, new_filename))
            count += 1

        print("Batch renaming completed successfully.")

    except Exception as e:
        print("Error:"+ e)

if __name__ == "__main__":
    print_banner()
    target_directory = raw_input("Enter the directory path: ").strip()
    file_prefix = raw_input("Enter the prefix for renamed files: ").strip()
    start_num = int(raw_input("Enter the starting number (default is 1): ") or 1)
    extension_filter = raw_input("Enter the file extension filter (e.g., .txt) or leave empty for all files: ").strip()
    extension_filter = extension_filter if extension_filter else None
    print("\nStarting mass renaming process...\n")
    mass_rename(target_directory, file_prefix, start_num, extension_filter)
