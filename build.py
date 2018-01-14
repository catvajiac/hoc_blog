#!/usr/bin/env python3

import markdown
import os
import pygments

if __name__ == "__main__":

  root = "./posts"
  with open("index.html", 'w+') as fwrite:
    with open("skeleton.html", 'r') as fread:
      line = fread.readline()
      while "</body>" not in line:
        fwrite.write(line)
        line = fread.readline()

    # append blogposts
    for file in os.listdir(root):
      if file[-3:] != ".md":
        continue
    
      name, ext = file.split(".")
  
      with open("{}/{}".format(root, file), 'r') as fread:
        for line in fread:
          fwrite.write(markdown.markdown(line))

    fwrite.write("  </body>\n")
    fwrite.write("</html>")
