#!/usr/bin/env python3

import markdown
import os
import pygments

if __name__ == "__main__":
  posts = "../pages"
  with open("../pages/skeleton.html", 'r') as fread:
    line = fread.readline().strip()
    while "</body>" not in line:
      print(line)
      line = fread.readline().strip()

  # append blogposts
  for file in os.listdir(posts):
    if file[-3:] != ".md":
      continue
  
    name, ext = file.split(".")

    print("<div class=blog_post>")
    with open("../pages/{}".format(file), 'r') as fread:
      for line in fread:
        print(markdown.markdown(line))
    print("</div>")

    print("</body>\n")
    print("</html>")
