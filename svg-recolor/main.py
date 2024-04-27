import svg
import re
import os
from config.definitions import ROOT_DIR

# fill_color = '(fill=".)[a-zA-Z0-9]*"'

def change_color(data_in):
    data_out = data_in
    fill_color = 'fill=".[a-zA-Z0-9]*"'
    stroke_color = 'stroke=".[a-zA-Z0-9]*"'
    value = '".[a-zA-Z0-9]*"'

    #-------- colors --------#
    green_replace = "#A7C080"
    red_replace = "#E67E80"
    grey_e0e0e0_replace = "#DBBC7F"
    grey_b3b3b3_replace = "#947538"
    white_fff_replace = "#83C092"
    white_ffffff_replace = "#9DA9A0"
    blue_replace = "#7FBBB3"
    purple_replace = "#D699B6"
    #------------------------#
    #-------- colors being replaced --------#
    # grey e0e0e0
    # grey b3b3b3
    # green 8eef97
    # white fff
    # red fc7f7f
    # blue 8da5f3
    # purple c38ef1
    
    if re.search(fill_color, data_in) != None:
        temp_fills = re.findall(fill_color, data)
        for fills in temp_fills:
            if "e0e0e0" in fills:
                temp_fill = fills.replace(re.search(value, fills).group(0).replace('"', ''), grey_e0e0e0_replace)
                data_out = data_out.replace(fills, temp_fill)
            if "b3b3b3" in fills:
                temp_fill = fills.replace(re.search(value, fills).group(0).replace('"', ''), grey_b3b3b3_replace)
                data_out = data_out.replace(fills, temp_fill)
            if "8eef97" in fills:
                temp_fill = fills.replace(re.search(value, fills).group(0).replace('"', ''), green_replace)
                data_out = data_out.replace(fills, temp_fill)
            if "fff" in fills:
                temp_fill = fills.replace(re.search(value, fills).group(0).replace('"', ''), white_fff_replace)
                data_out = data_out.replace(fills, temp_fill)
            if "ffffff" in fills:
                temp_fill = fills.replace(re.search(value, fills).group(0).replace('"', ''), white_ffffff_replace)
                data_out = data_out.replace(fills, temp_fill)
            if "fc7f7f" in fills:
                temp_fill = fills.replace(re.search(value, fills).group(0).replace('"', ''), red_replace)
                data_out = data_out.replace(fills, temp_fill)
            if "8da5f3" in fills:
                temp_fill = fills.replace(re.search(value, fills).group(0).replace('"', ''), blue_replace)
                data_out = data_out.replace(fills, temp_fill)
            if "c38ef1" in fills:
                temp_fill = fills.replace(re.search(value, fills).group(0).replace('"', ''), purple_replace)
                data_out = data_out.replace(fills, temp_fill)
    if re.search(stroke_color, data) != None:
        temp_strokes = re.findall(stroke_color, data)
        for strokes in temp_strokes:
            if "e0e0e0" in strokes:
                stroke_fill = strokes.replace(re.search(value, strokes).group(0).replace('"', ''), grey_e0e0e0_replace)
                data_out = data_out.replace(strokes, stroke_fill)
            if "b3b3b3" in strokes:
                stroke_fill = strokes.replace(re.search(value, strokes).group(0).replace('"', ''), grey_b3b3b3_replace)
                data_out = data_out.replace(strokes, stroke_fill)
            if "8eef97" in strokes:
                stroke_fill = strokes.replace(re.search(value, strokes).group(0).replace('"', ''), green_replace)
                data_out = data_out.replace(strokes, stroke_fill)
            if "fff" in strokes:
                stroke_fill = strokes.replace(re.search(value, strokes).group(0).replace('"', ''), white_fff_replace)
                data_out = data_out.replace(strokes, stroke_fill)
            if "ffffff" in strokes:
                stroke_fill = strokes.replace(re.search(value, strokes).group(0).replace('"', ''), white_ffffff_replace)
                data_out = data_out.replace(strokes, stroke_fill)
            if "fc7f7f" in strokes:
                stroke_fill = strokes.replace(re.search(value, strokes).group(0).replace('"', ''), red_replace)
                data_out = data_out.replace(strokes, stroke_fill)
            if "8da5f3" in strokes:
                stroke_fill = strokes.replace(re.search(value, strokes).group(0).replace('"', ''), blue_replace)
                data_out = data_out.replace(strokes, stroke_fill)
            if "c38ef1" in strokes:
                stroke_fill = strokes.replace(re.search(value, strokes).group(0).replace('"', ''), purple_replace)
                data_out = data_out.replace(strokes, stroke_fill)

    return data_out

def get_all_colors(filse_list):
    fill_colors = set()
    stroke_colors = set()
    fill_color = '(fill=".)[a-zA-Z0-9]*"'
    stroke_color = '(stroke=".)[a-zA-Z0-9]*"'
    value = '".[a-zA-Z0-9]*"'

    for file in filse_list:
        file_path = "svgs/" + file
        open_file = open(file_path, "rt")
        data = open_file.read()
        if re.search(fill_color, data) != None:
            fill_colors.add(re.search(value, re.search(fill_color, data).group(0)).group(0).replace('"', '').replace("#", ''))
        if re.search(stroke_color, data) != None:
            stroke_colors.add(re.search(value, re.search(stroke_color, data).group(0)).group(0).replace('"', '').replace("#", ''))
        open_file.close()
    
    file_to_write = open('fill_colors.txt', 'w')
    for lines in fill_colors:
        file_to_write.write(lines + "\n")
    file_to_write.close()
    file_to_write = open('stroke_colors.txt', 'w')
    for lines in stroke_colors:
        file_to_write.write(lines + "\n")
    file_to_write.close()
    print(fill_colors)
    print(stroke_colors)

#icon_paths = []
#icon_paths.append("modules/regex/icons/")
#icon_paths.append("modules/gdscript/icons/")
#icon_paths.append("misc/dist/document_icons/")
#icon_paths.append("modules/mono/icons/")
#icon_paths.append("modules/csg/icons/")
#icon_paths.append("scene/theme/icons/")
#icon_paths.append("editor/icons/")

print("Enter the path to your main godot folder")
print("for example if you downloaded 4.2 and unzipped the source directly to the C drive it would be C:/godot-4.2/")
godot_path = input(": ").strip()

end_slash_regex = "/$"
if re.match(end_slash_regex, godot_path) == None:
    godot_path = godot_path + "/"

file = open(os.join(ROOT_DIR, 'icon_paths.txt', 'r'))
icon_paths = file.readlines()
file.close()
iterator = 0
for n in range(0, 6):
    icon_paths[iterator] = n.replace('\n', '')
    iterator += 1
file = open(os.join(ROOT_DIR, "excludes.txt", 'r'))
excludes_list = file.readlines()
file.close()

for icon_folder in icon_paths:
    svg_list = os.listdir(icon_folder)

    for files in svg_list:
        if ".svg" in files:
            #print('found svgs')
            file = open(icon_folder + files, "rt")
            data = file.read()
            file.close()
            is_excluded = False
            for exclude in excludes_list:
                if file == exclude:
                    is_excluded = True
            if not is_excluded:
                print('changed color in file %s' % icon_folder)
                temp_data = change_color(data)
                is_excluded = False
            

            write_to_file = open(icon_folder + files, "wt")
            write_to_file.write(temp_data)
            write_to_file.close()

print("done")