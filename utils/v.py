import os

def get_all_file_names(root_dir):
    """
    Recursively collects all file names from the given directory and its subdirectories.

    Parameters:
    - root_dir (str): The path of the root directory to start searching from.

    Returns:
    - List[str]: A list of all file names found within the directory hierarchy.
    """
    file_names = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            # If you need the full path, use os.path.join(root, file) instead
            file_names.append(file)
    return file_names

# Example usage
root_directory = r"C:\Users\User\PycharmProjects\pythonProject"  # Replace with your directory path
all_file_names = get_all_file_names(root_directory)
print(all_file_names)
