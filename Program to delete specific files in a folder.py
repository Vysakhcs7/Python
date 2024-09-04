import os

def delete_files_with_extension(root_folder, extension):
    """
    Deletes files with a specific extension inside a folder and its subfolders.

    Parameters:
    root_folder (str): Path to the parent folder.
    extension (str): Extension of the files to be deleted.
    """
    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith(extension):
                file_path = os.path.join(foldername, filename)
                os.remove(file_path)
                print(f"{filename} has been deleted from {foldername}.")

# Example usage:
parent_folder = r"D:\Udemy Courses\Udemy - ARM Cortex M Microcontroller DMA Programming Demystified 2022-8"
extension = ".vtt"

delete_files_with_extension(parent_folder, extension)
