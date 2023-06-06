import os
import sys
import shutil
from pathlib import Path

src_path = r"gemini"
dst_path = r"html"
shutil.copytree(src_path, dst_path)

directory = os.path.dirname(os.path.realpath(sys.argv[0])) #get the directory of your script
print(directory)
for subdir, dirs, files in os.walk("html"):
 for filename in files:
  if filename.find('.gmi') > 0:
   subdirectoryPath = os.path.relpath(subdir, directory) #get the path to your subdirectory
   print(subdirectoryPath)
   filePath = os.path.join(subdirectoryPath, filename) #get the path to your file
   destination= open(filePath.replace(".gmi",".html"), "w")
   source= open(filePath, "r")
   destination.write("<!DOCTYPE html>\n")
   destination.write("<html>\n")
   destination.write("<head>\n")
   destination.write("<title></title>\n")
   destination.write("<link rel=\"stylesheet\" href=\"style.css\">\n")
   destination.write("</head>\n")
   destination.write("<body>\n")
   for line in source:
    if line.startswith('###'):
     destination.write("<h3>")
     destination.write(line[3:len(line)].strip())
     destination.write("</h3>\n")
    elif line.startswith('##'):
     destination.write("<h2>")
     destination.write(line[2:len(line)].strip())
     destination.write("</h2>\n")
    elif line.startswith('#'):
     destination.write("<h1>")
     destination.write(line[1:len(line)].strip())
     destination.write("</h1>\n")
    elif line.startswith('=>'):
     if line[2:len(line)].strip().split(" ", 1)[0].endswith(('.apng', '.gif', '.ico', '.cur', '.jpg', '.jpeg', '.jfif', '.pjpeg', '.pjp', '.png', '.svg')):
      destination.write("<img scr=\"")
      destination.write(line[2:len(line)].strip().split(" ", 1)[0])
      if len(line[2:len(line)].strip().split(" ", 1))>1:
       destination.write("\" alt=\"")
       destination.write(line[2:len(line)].strip().split(" ", 1)[1])
       destination.write("\">\n")
       destination.write("<p>")
       destination.write(line[2:len(line)].strip().split(" ", 1)[1])
       destination.write("</p>\n")
      else:
       destination.write("\">\n")
     else:
      destination.write("<a href=\"")
      if line.startswith('gemini://'):
       destination.write(line[2:len(line)].strip().split(" ", 1)[0])
      else:
       destination.write(line[2:len(line)].strip().split(" ", 1)[0].replace(".gmi",".html"))
      destination.write("\">")
     if len(line[2:len(line)].strip().split(" ", 1))>1:
      destination.write(line[2:len(line)].strip().split(" ", 1)[1])
     else:
      destination.write(line[2:len(line)].strip().split(" ", 1)[0])
     destination.write("</a>\n")
    else:
     destination.write("<p>")
     destination.write(line.strip())
     destination.write("</p>\n")

   destination.write("</body>\n")
   destination.write("</html>\n")
   source.close()
   destination.close()
   os.remove(filePath)
