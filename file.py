import os, shutil
path = input("Enter the file path")
file_name = os.listdir(path)

file_format_list = []
for file in file_name:
  s = file.rsplit(',')[-1]
  file_format_list.append(s)
  unique_list = list(set(file_format_list))

for file in file_name:
if ".pptx" in file and not os.path.exists(path3+"pptx file/"+file):
    shutil.move(path + file, path3 + "pptx file/" + file)

elif ".pdf" in file and not os.path.exists(path3 + "pdf file/"+file):
    shutil.move(path + file, path3 + "pdf file/" + file)
elif ".jpg" in file and not os.path.exists(path3 + "jpg file/"+file):
    shutil.move(path + file, path3 + "jpg file/" + file)
elif ".docx" in file and not os.path.exists(path3 + "docx file/"+file):
    shutil.move(path + file, path3 + "docx file/" + file)
elif ".jpeg" in file and not os.path.exists(path3 + "jpeg file/"+file):
    shutil.move(path + file, path3 + "jpeg file/" + file)
elif ".png" in file and not os.path.exists(path3 + "png file/"+file):
    shutil.move(path + file, path3 + "png file/" + file)
else:
    print("File type not found")
print("Done!")