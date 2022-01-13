import os

os.chdir("C:/Users/starw/Music/task_music")

for file in os.listdir():
    file_name, file_ext = os.path.splitext(file)
    ymate, f_name = file_name.split(" - ")

    new_name = "{}{}".format(f_name, file_ext)
    os.rename(file, new_name)

