import os
import shutil

def dupe(numberOf, fldr):
    y = 0
    dir = "my_folder"
    for path in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, path)):
            y += 1
    x = y + 1
    while get_directory_size('my_folder') <= numberOf:
        savePath = "my_folder/glizzy" + str(x) + ".jpeg"
        shutil.copy('glizzy.jpeg', savePath)
        x += 1
        numberOf -= 1

def get_directory_size(directory):
    total = 0
    try:
        for entry in os.scandir(directory):
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_directory_size(entry.path)
    except NotADirectoryError:
        return os.path.getsize(directory)
    except PermissionError:
        return 0
    return total

def get_size_format(b, factor=1024, suffix="B"):
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"
