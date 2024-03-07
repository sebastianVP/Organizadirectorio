import os 
import shutil
import sys

def directory(file_extension):

    if not file_extension:
       return
    folders_by_extension = {
        "exe"  : "Sofware",
        "txt"  : "Texts",
        "jpg"  : "Images",
        "jpeg" : "Images",
        "png"  : "Images",
        "rar"  : "Compressed Files",
        "zip"  : "Compressed Files",
        "ppt"  : "PresentacionPPT",
        "pptx" : "PresentacionPPT",
        "doc"  : "OfficeWord",
        "docx" : "OfficeWord",
        "xlsx" : "ExcelFiles",
        "xlsm" : "ExcelFiles",
        "pdf"  : "PDFDocuments",
        "py"   : "PYTHONScripts",
        "mp3"  : "MUSIC",
        "mp4"  : "MUSIC"
      }
    return folders_by_extension.get(file_extension,'Extras')

def organize(path):

    if not os.path.exists(path):
       print(f"ERROR, Not found {path0} or not exists")
       return
    files= os.listdir(path)
    extensions = [os.path.splitext(file)[1].strip(".") for file in files]


    for ext in extensions:
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


if __name__ == "__main__":
  try:
    directory_location = sys.argv[1]
    organize(directory_location)
  except Exception as e:
    print(f"There was an error:{str(e)}")


# python file_organizer.py /home/soporte/Downloads
