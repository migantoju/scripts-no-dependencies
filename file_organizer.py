# Author: Miguel Toledano
import os
import shutil
import sys


# define a dict with type extension and type of file
def directory(file_extension: str) -> str:
    # If there is not a file_extension passed to the
    # function, then we get out of the exec.
    if not file_extension:
        return
    # a dictionary that contains file ´extension´ : ´folder name´
    # where we will move those files depending on there extension.
    folders_by_extension = {
        "exe": "Software",
        "txt": "Texts",
        "pdf": "PDF Documents",
        "epub": "Books",
        "jpg": "Images",
        "jpeg": "Images",
        "png": "Images",
        "raw": "Images",
        "mp3": "Music",
        "mp4": "Videos",
        "mkv": "Videos",
        "xlsx": "Excel Files",
        "ppt": "Slides",
        "doc": "Documents",
        "rar": "Compressed Files",
        "zip": "Compressed Files"
    }
    # If there's a file that haven't defined above, then
    # it will be moved into Extras folder.
    return folders_by_extension.get(file_extension, 'Extras')


def organize(path: str):
    """
    Main method that allows us to organize the files of a 
    specific path on our computer, depending on the type of 
    extension that the file has.
    Parameters
    --------------
    path : str
        The url or location on the computer
    Returns
    --------------
        None
    """
    if not os.path.exists(path):
        print(f"ERROR. Not found {path} or not exists.")
        return

    files = os.listdir(path)
    extensions = [os.path.splitext(file)[1].strip(".") for file in files]

    # check if directory exists, if not, create.
    for ext in extensions:
        dir = directory(ext) or ""
        new_directory = os.path.join(path, dir)
        if dir and not os.path.exists(new_directory):
            os.makedirs(new_directory)

    # Now it's time to move the files to the new folders.
    for file in files:
        ext = os.path.splitext(file)[1].strip(".")
        _dir = directory(ext)
        if not _dir:
            continue

        source_filepath = os.path.join(path, file)
        print(source_filepath)
        destination_filepath = os.path.join(path, _dir, file)
        print(destination_filepath)

        if not os.path.exists(destination_filepath):
            shutil.move(source_filepath, destination_filepath)
            print(f"Was moved {file} into {_dir} directory. \n")
    print(f"All the files was organized successfully in {path}")


if __name__ == "__main__":
    try:
        directory_location = sys.argv[1]
        organize(directory_location)
    except Exception as e:
        print(f"There was an error: {str(e)}")
