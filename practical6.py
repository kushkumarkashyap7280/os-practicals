import os
import stat
import sys
import time

def get_file_details(file_path):
    try:
        # Get file stat information
        file_stat = os.stat(file_path)

        # Extract file details
        owner_permission = stat.S_IMODE(file_stat.st_mode) >> 6 & 0o7
        access_time = time.ctime(file_stat.st_atime)

        return owner_permission, access_time
    except FileNotFoundError:
        return None, None

def main():
    if len(sys.argv) != 2:
        print("Usage: python file_details.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    owner_permission, access_time = get_file_details(file_path)

    if owner_permission is not None:
        print(f"File: {file_path}")
        print(f"Owner Access Permissions: {owner_permission}")
        print(f"File Access Time: {access_time}")
    else:
        print(f"File not found: {file_path}")

if __name__ == "__main__":
    main()