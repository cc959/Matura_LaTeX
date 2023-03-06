path = "/home/elias/Documents/ParabPaths/2023-02-26 16:52:11.txt"
# path = "/home/elias/Documents/ParabPaths/2023-02-26 15:00:37.txt"
path = "/home/elias/Documents/ParabPaths/2023-02-28 19:13:08.txt"
file = open(path, "r")

lines = file.readlines()

type = -1

funcsX = []
funcsY = []
funcsZ = []
pointsX = ""
pointsY = ""
pointsZ = ""

# parse the file
for line in lines:
    if line[0] == 't':
        type += 1
        continue
    if line.__contains__('x'):
        line = line.rstrip(" \n")
        if type == 0:
            funcsX.append(line)
        if type == 1:
            funcsY.append(line)
        if type == 2:
            funcsZ.append(line)
    else:
        if type == 0:
            pointsX += line
        if type == 1:
            pointsY += line
        if type == 2:
            pointsZ += line

headerX = "\\newcommand{\\FlightPathX}[1][1]{\n\t\\begin{tikzpicture} [scale = #1, trim axis left, trim axis right]\n\t\t\\begin{axis} [\n\t\t\t\txmin = -0.1, xmax = 0.7,\n\t\t\t\tymin = -3, ymax= 3,\n\t\t\t\tgrid=major, % Display a grid\n\t\t\t\tgrid style={dashed, red!30},\n\t\t\t\txlabel=Zeit,\n\t\t\t\tylabel=Position,\n\t\t\t\tx unit=\\si{\\second},\n\t\t\t\ty unit=\\si{\\meter},\n\t\t\t]\n"
headerY = "\\newcommand{\\FlightPathY}[1][1] {\n\t\\begin{tikzpicture} [scale = #1, trim axis left, trim axis right]\n\t\t\\begin{axis} [\n\t\t\t\txmin = -0.1, xmax = 0.7,\n\t\t\t\tymin = -3, ymax = 3,\n\t\t\t\tgrid=major, % Display a grid\n\t\t\t\tgrid style={dashed, green!30},\n\t\t\t\txlabel=Zeit,\n\t\t\t\tylabel=Position,\n\t\t\t\tx unit=\\si{\\second}, % Set the respective units\n\t\t\t\ty unit=\\si{\\meter},\n\t\t\t]\n"
headerZ = "\\newcommand{\\FlightPathZ}[1][1] {\n\t\\begin{tikzpicture} [scale = #1, trim axis left, trim axis right]\n\t\t\\begin{axis} [\n\t\t\t\txmin = -0.1, xmax = 0.7,\n\t\t\t\tymin = 0.3, ymax = 1.3,\n\t\t\t\tgrid=major, % Display a grid\n\t\t\t\tgrid style={dashed, blue!30},\n\t\t\t\txlabel=Zeit,\n\t\t\t\tylabel=Höhe,\n\t\t\t\tx unit=\\si{\\second}, % Set the respective units\n\t\t\t\ty unit=\\si{\\meter},\n\t\t\t]\n"
header3D = "\\newcommand{\\FlightPath}[1][1] {\n\t\\begin{tikzpicture} [scale = #1]\n\t\t\\begin{axis}\n\t\t\t[view={-60}{30},\n\t\t\t\tymin=-0.8,ymax=0,\n\t\t\t\tgrid=major, % Display a grid\n\t\t\t\tgrid style={dashed, purple!30},\n\t\t\t\txlabel=X Position,\n\t\t\t\tylabel=Y Position,\n\t\t\t\tzlabel=Höhe,\n\t\t\t\tx unit=\\si{\\meter}, % Set the respective units\n\t\t\t\ty unit=\\si{\\meter},\n\t\t\t\tz unit=\\si{\\meter},\n\t\t\t]\n"

footerX = "\t\t\t\\addplot[\n\t\t\t\tdomain = 0:0.7,\n\t\t\t\tsmooth,\n\t\t\t\tonly marks,\n\t\t\t\tred,\n\t\t\t] file[skip first] {../resources/blub/FlightPathX.dat};\n\n\n\t\t\\end{axis}\n\t\\end{tikzpicture}\n}"
footerY = "\t\t\t\\addplot[\n\t\t\t\tdomain = 0:0.7,\n\t\t\t\tsmooth,\n\t\t\t\tonly marks,\n\t\t\t\tgreen,\n\t\t\t] file[skip first] {../resources/blub/FlightPathY.dat};\n\n\n\t\t\\end{axis}\n\t\\end{tikzpicture}\n}"
footerZ = "\t\t\t\\addplot[\n\t\t\t\tdomain = 0:0.7,\n\t\t\t\tsmooth,\n\t\t\t\tonly marks,\n\t\t\t\tblue,\n\t\t\t] file[skip first] {../resources/blub/FlightPathZ.dat};\n\n\n\t\t\\end{axis}\n\t\\end{tikzpicture}\n}"
footer3D = "\t\t\t\\addplot3[\n\t\t\t\tmark=*,\n\t\t\t\tblue,\n\t\t\t\tmark options={\n\t\t\t\t\t\tdraw=black,\n\t\t\t\t\t\tfill=purple,\n\t\t\t\t\t},\n\t\t\t] file{../resources/blub/FlightPath3D.dat};\n\t\t\\end{axis}\n\t\\end{tikzpicture}\n}"

output = ""

steps = 2

output += headerX
for i, func in enumerate(funcsX[::steps]):
    output += "\\addplot[\n\t\t\t\tdomain = -1:1,\n\t\t\t\tsmooth,\n\t\t\t\tultra thick,\n\t\t\tdotted,\n\t\t\t\tgray!" + \
        str((i + 5) * 100 * steps // len(funcsX)) + "\n\t\t\t] {" + func + "};"

output += "\\addplot[\n\t\t\t\tdomain = -1:1,\n\t\t\t\tsmooth,\t\t\t\tultra thick,\n\t\t\t\tred!50\n\t\t\t] {" + funcsX[-1] + "};\n\n"
output += footerX

output += headerY
for i, func in enumerate(funcsY[::steps]):
    output += "\\addplot[\n\t\t\t\tdomain = -1:1,\n\t\t\t\tsmooth,\n\t\t\t\tultra thick,\n\t\t\tdotted,\n\t\t\t\tgray!" + \
        str((i + 5) * 100 * steps // len(funcsY)) + "\n\t\t\t] {" + func + "};"

output += "\\addplot[\n\t\t\t\tdomain = -1:1,\n\t\t\t\tsmooth,\n\t\t\t\tultra thick,\n\t\t\t\tgreen!50\n\t\t\t] {" + funcsY[-1] + "};]\n\n"
output += footerY

output += headerZ
for i, func in enumerate(funcsZ[::steps]):
    output += "\\addplot[\n\t\t\t\tdomain = -1:1,\n\t\t\t\tsmooth,\n\t\t\t\tultra thick,\n\t\t\tdotted,\n\t\t\t\tgray!" + \
        str((i + 5) * 100 * steps // len(funcsZ)) + "\n\t\t\t] {" + func + "};"

output += "\\addplot[\n\t\t\t\tdomain = -1:1,\n\t\t\t\tsmooth,\n\t\t\t\tultra thick,\n\t\t\t\tblue!50\n\t\t\t] {" + funcsZ[-1] + "};\n\n"
output += footerZ

output += header3D

points_seperate = []

for pointX in pointsX.split("\n"):
    points_seperate.append(pointX.split(" ")[-1])

for i, pointY in enumerate(pointsY.split("\n")):
    points_seperate[i] += " " + pointY.split(" ")[-1]

for i, pointZ in enumerate(pointsZ.split("\n")):
    points_seperate[i] += " " + pointZ.split(" ")[-1]

points3D = ""

for point_seperate in points_seperate:
    points3D += point_seperate + "\n"

for i in range(0, len(funcsX), 5):
    output += "\t\t\t\\addplot3+[no markers, samples=25, samples y=0, smooth, dotted, ultra thick, domain = 0:1, variable =\\t, gray!" + str(i * 100 // len(
        funcsX)) + "] ({" + funcsX[i].replace("x", "\\t") + "}, {" + funcsY[i].replace("x", "\\t") + "}, {" + funcsZ[i].replace("x", "\\t") + "});\n\n"

output += "\t\t\t\\addplot3+[no markers, samples=25, samples y=0, smooth, solid, ultra thick, domain = 0:1, variable =\\t, purple] ({" + funcsX[-1].replace(
    "x", "\\t") + "}, {" + funcsY[-1].replace("x", "\\t") + "}, {" + funcsZ[-1].replace("x", "\\t") + "});\n\n"


output += footer3D

FlightPaths = open("./FlightPaths.tex", "w")
FlightPathX = open("./FlightPathX.dat", "w")
FlightPathY = open("./FlightPathY.dat", "w")
FlightPathZ = open("./FlightPathZ.dat", "w")
FlightPath3D = open("./FlightPath3D.dat", "w")

FlightPaths.write(output)
FlightPaths.close()

FlightPathX.write(pointsX)
FlightPathX.close()

FlightPathY.write(pointsY)
FlightPathY.close()

FlightPathZ.write(pointsZ)
FlightPathZ.close()

FlightPath3D.write(points3D)
FlightPath3D.close()
