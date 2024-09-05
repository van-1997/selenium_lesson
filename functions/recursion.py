
import os
def files(directory):
    file_list = []
    def recurse(directory):
        for entry in os.scandir(directory):
            if entry.is_file():
                file_list.append(entry.path)
            elif entry.is_dir():
                recurse(entry.path)

    recurse(directory)
    return file_list

all_files = files('dir1')
print("vse fayli :",len(all_files),"-",all_files)