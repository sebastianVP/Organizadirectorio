import os 
import shutil
import sys

def directory(file_extension):

    if not file_extension:
       return
    folders_by_extension = {
        "exe"  = "Sofware",
        "txt"  = "Texts",
        "jpg"  = "Images",
        "jpeg" = "Images",
        "png"  = "Images",
        "rar"  = "Compressed Files",
        "zip"  = "Compressed Files",
        "ppt"  = "PresentacionPPT",
        "pptx" = "PresentacionPPT",
        "doc"  = "OfficeWord",
        "dodx" = "OfficeWord",
        "xlsx" = "ExcelFiles",
        "pdf"  = "PDFDocuments"
      }
    return foldes_by_extesion.get(file_extension,'Extras')

def organize(path):

    if not os.path.exits(path):
       print(f"ERROR, Not found {path0} or not exists")
       return
    files= os.listdir(path)
    extensions = [os.path.splitext(file)[1].strip("."") for file in files]


    for ext in extension:
        dir =  directory(ext) or ""
        new_directory = os.path.join(path,dir)
        if dir and not os.path.exists(new_directory):
           os.makedirs(new_directory)
    for file in files:
       ext = os.path.splitext(file)[1].strip(".")
       _dir = directory(ext)
       if not _dir:
         continue
      
       source_filepath = os.path.join(path,file)
       destination_filepath = os.path.join(path,_dir,file)
       if not os.path.exists(destination_filepath):
          shutil.move(source_filepath,destination_filepath)
          print(f"Was moved {file} into {_dir} directory. \n")
    print(f"All the files was organized succesfully in {path}")

