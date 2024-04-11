import os
import re

svg_list = os.listdir("svgs/")
fill_color = 'fill=".[a-zA-Z0-9]*"'
stroke_color = 'stroke=".[a-zA-Z0-9]*"'

for files in svg_list:
    file = open("svgs/" + files)
    data = file.read()
    file.close()

    if re.search(fill_color, data) != None:
        temp_fills = re.findall(fill_color, data)
        for fills in temp_fills:
            if "e0e0e0" in fills:
                print(files)
    if re.search(stroke_color, data) != None:
        temp_fills = re.findall(stroke_color, data)
        for fills in temp_fills:
            if "e0e0e0" in fills:
                print(files)