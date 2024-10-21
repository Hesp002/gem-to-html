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
   #print(subdirectoryPath)
   filePath = os.path.join(subdirectoryPath, filename) #get the path to your file
   destination= open(filePath.replace(".gmi",".html"), "w")
   source= open(filePath, "r")
   destination.write("<!DOCTYPE html>\n")
   destination.write("<html>\n")
   destination.write("<head>\n")
   destination.write("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\" />\n")
   destination.write("<title>HES.PE</title>\n")
   destination.write("<link rel=\"icon\" type=\"image/x-icon\" href=\"/favicon.ico\">\n")
   destination.write("<link rel=\"stylesheet\" href=\"/style.css\">\n")
   destination.write("</head>\n")
   destination.write("<body>\n")
   destination.write("<div class=\"main\">\n")
   monospaceText = False
   listText = False
   for line in source:
    checkbox = False
    if line.startswith('* [ ] '):
     destination.write("<div class=\"text\"><label class=\"checkbox\"><input type=\"checkbox\" disabled>")
     destination.write(line[6:len(line)].strip())
     destination.write("</label></div>\n")
     checkbox = True
    elif line.startswith('* [x] '):
     destination.write("<div class=\"text\"><label class=\"checkbox\"><input type=\"checkbox\" checked=\"checked\" disabled>")
     destination.write(line[6:len(line)].strip())
     destination.write("</label></div>\n")
     checkbox = True
    elif line.startswith('*') and not listText:
     destination.write("<div class=\"list\"><ul>\n")
     destination.write("<li>")
     destination.write(line[1:len(line)])
     destination.write("</li>\n")
     listText = True
    elif line.startswith('*') and listText:
     destination.write("<li>")
     destination.write(line[1:len(line)])
     destination.write("</li>\n")
    elif listText:
     destination.write("</ul></div>\n")
     listText = False
    if line.startswith('```') and not monospaceText:
     destination.write("<!-- ")
     destination.write(line[3:len(line)].strip())
     destination.write(" -->\n")
     destination.write("<div class=\"monospace\"><pre>")
     monospaceText = True
    elif line.startswith('```') and monospaceText:
     destination.write("</pre></div>")
     monospaceText = False
    elif monospaceText:
     destination.write(line)
    elif line.startswith('###'):
     destination.write("<div class=\"header3\"><h3>")
     destination.write(line[3:len(line)].strip())
     destination.write("</h3></div>\n")
    elif line.startswith('##'):
     destination.write("<div class=\"header2\"><h2>")
     destination.write(line[2:len(line)].strip())
     destination.write("</h2></div>\n")
    elif line.startswith('#'):
     destination.write("<div class=\"header1\"><h1>")
     destination.write(line[1:len(line)].strip())
     destination.write("</h1></div>\n")
    elif line.startswith('=>'):
     if line[2:len(line)].strip().split(" ", 1)[0].endswith(('.apng', '.gif', '.ico', '.cur', '.jpg', '.jpeg', '.jfif', '.pjpeg', '.pjp', '.png', '.svg')):
      destination.write("<div class=\"image\"><img src=\"")
      destination.write(line[2:len(line)].strip().split(" ", 1)[0])
      if len(line[2:len(line)].strip().split(" ", 1))>1:
       destination.write("\" alt=\"")
       destination.write(line[2:len(line)].strip().split(" ", 1)[1])
       destination.write("\"></div>\n")
       destination.write("<div class=\"imagetext\"><span>")
       destination.write(line[2:len(line)].strip().split(" ", 1)[1])
       destination.write("</span></div>\n")
      else:
       destination.write("\"></div>\n")
     else:
      if "http://" in line or "https://" in line:
       destination.write("<div class=\"link\"><a href=\"")
       destination.write(line[2:len(line)].strip().split(" ", 1)[0])
      elif "://" in line:
       destination.write("<div class=\"outsidelink\"><a href=\"")
       destination.write(line[2:len(line)].strip().split(" ", 1)[0])
      else:
       destination.write("<div class=\"link\"><a href=\"")
       destination.write(line[2:len(line)].strip().split(" ", 1)[0].replace(".gmi",".html"))
      destination.write("\">")
      if len(line[2:len(line)].strip().split(" ", 1))>1:
       destination.write(line[2:len(line)].strip().split(" ", 1)[1])
      else:
       destination.write(line[2:len(line)].strip().split(" ", 1)[0])
      destination.write("</a></div>\n")
    elif line.startswith('>'):
     destination.write("<div class=\"quote\"><p>")
     destination.write(line.strip())
     destination.write("</p></div>\n")
    elif not listText and not checkbox and len(line.strip())>0:
     destination.write("<div class=\"text\"><p>")
     destination.write(line.strip())
     destination.write("</p></div>\n")

   destination.write("<div class=\"notice\"><span>")
   destination.write("This webpage was <a href=\"https://github.com/Hesp002/gem-to-html\">automatically converted</a> from my gemini capsule, there might be some issues. <a href=\"https://geminiprotocol.net/docs/faq.gmi\">What is Gemini?</a> Learn more <a href=\"https://geminiprotocol.net/\">here</a>.")
   destination.write("<span><div>\n")
   destination.write("</div>\n")
   destination.write("</body>\n")
   destination.write("</html>\n")
   source.close()
   destination.close()
   os.remove(filePath)

print("Created html files for mirror")
