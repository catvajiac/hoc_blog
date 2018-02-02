#!/usr/bin/env python3

#import markdown
import pypandoc
import os

if __name__ == "__main__":
  posts = "../pages"
  with open("../pages/skeleton.html", 'r') as fread:
    line = fread.readline().strip()
    while "</body>" not in line:
      print(line)
      line = fread.readline().strip()

  # append blogposts
  for file in sorted(os.listdir(posts), reverse=True):
    if file[-3:] != ".md":
      continue
  
    name, ext = file.split(".")
    entry = name[-2:]

    print("<div class=blog_post id=#{}>".format(entry))
    print("<h3>{}</h3>".format(name).title())
    print(pypandoc.convert_file("../pages/{}".format(file), 'html'))
    print("</div>")

    print("</body>\n")
    print("</html>")
