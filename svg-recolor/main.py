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

file = open(os.path.join(ROOT_DIR, 'icon_paths.txt'), 'r')
icon_paths = file.readlines()
file.close()
iterator = 0
for n in icon_paths:
    icon_paths[iterator] =godot_path + n.replace('\n', '')
    iterator += 1
file = open(os.path.join(ROOT_DIR, "excludes.txt"), 'r')
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
            
            if files == "Signals.svg":
                temp_data = '<svg height="16" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="m4 2a1 1 0 0 0 0 2 8 8 0 0 1 8 8 1 1 0 0 0 2 0 10 10 0 0 0 -10-10zm0 4a1 1 0 0 0 0 2 4 4 0 0 1 4 4 1 1 0 0 0 2 0 6 6 0 0 0 -6-6zm0 4a2 2 0 0 0 0 4 2 2 0 0 0 0-4z" fill="#dbbc7f"/><g stroke-width=".013434"><path d="m3.7816961 13.983232c-.3657574-.055475-.6351727-.157342-.9135181-.345405-.1669729-.112814-.4071523-.355848-.5209633-.527154-.4029887-.60657-.4503247-1.357725-.1261874-2.002417.098175-.195265.2172218-.35996.3722453-.514983.7613445-.7613448 1.983569-.7820374 2.7646021-.04681.2418126.227632.4153461.493189.5246118.802807.080882.229188.1014216.362478.1007956.654085-.0004658.216954-.00553.284506-.029446.393162-.1753438.796472-.7679386 1.388677-1.5573152 1.55629-.1276303.0271-.5114907.04609-.6148251.03042z" fill="#e67e80"/><g fill="#a7c080"><path d="m8.8544966 12.981883c-.3115294-.044549-.5968672-.250821-.7402217-.53511-.0764166-.151543-.0951175-.242189-.1081095-.524019-.023193-.503122-.0807316-.824806-.2204915-1.232716-.1977863-.57727-.5043802-1.0660138-.9467433-1.5092129-.3448268-.3454785-.6403756-.5595812-1.0555553-.7646701-.5505366-.2719519-.9989896-.3857471-1.640659-.4163182-.3210667-.0152966-.4364497-.0378948-.5888832-.1153348-.488615-.2482289-.6820713-.8353392-.4378034-1.3286666.0997026-.2013609.2500887-.3481988.4621911-.4512861.1762429-.0856587.2599452-.0976911.6188472-.0889609 1.1629625.028289 2.3103345.4148823 3.2808709 1.105451.4669953.3322825.9359729.7869544 1.2927662 1.2533317.7646611.999516 1.2108594 2.2913079 1.2163673 3.5215149.0009632.215154-.0032.277568-.023315.349286-.1112064.396555-.4339979.68221-.8337257.737807-.1179681.01641-.1541359.01626-.2755352-.0011z"/><path d="m12.82511 12.976904c-.359318-.0678-.652288-.323569-.768931-.671278-.03285-.09794-.03711-.134891-.048-.416457-.02196-.56776-.06529-.980155-.147509-1.403863-.274738-1.4158084-.916345-2.7183281-1.8712892-3.7988758-.1898858-.2148614-.5940232-.6097487-.813898-.7952689-1.1310036-.9542889-2.4730879-1.5679708-3.9361881-1.7998624-.3571671-.0566086-.6095988-.0792002-1.054576-.09438-.2917896-.009954-.3658357-.0166371-.4498225-.0405986-.2690721-.076767-.4994223-.2678312-.6221559-.5160479-.0794686-.1607176-.0969305-.2429384-.0958219-.4511876.0008345-.1567674.0056025-.1953264.0351614-.2843547.0546203-.1645106.1232729-.273918.2514899-.4007838.1320938-.1307018.2205793-.1870701.3872956-.2467206l.1176989-.042112.3694375.0009292c1.1349028.00285 2.3442316.2405504 3.4667608.6813977 1.4666594.5759964 2.7565345 1.4750295 3.8256405 2.666443.361064.4023707.770628.9574829 1.072704 1.4539169.916624 1.5063867 1.429107 3.2902505 1.445365 5.0310655.0025.272556.000371.303853-.02795.402263-.05239.182019-.126606.307222-.263928.44523-.10278.103293-.14106.13167-.249069.184639-.07019.03442-.162999.07152-.206235.08244-.121194.0306-.29548.03624-.416178.01347z"/></g></g></svg>'
                print('changed color in file %s' % icon_folder)
                
            write_to_file = open(icon_folder + files, "wt")
            write_to_file.write(temp_data)
            write_to_file.close()

print("done")