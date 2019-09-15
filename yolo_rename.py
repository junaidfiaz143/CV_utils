from xml.etree import ElementTree as et
import os

output_list = []

def create_output_file():
    output_file = open("train_output.txt", "w+")

    for output in output_list:
    	output_file.write(output + "\n")

    output_file.close()

def update_xml(path, filename):
    tree = et.parse(path)

    # tree.find(".//filename").text = filename.split(".")[0]+".jpg"

    # print("+-----------------+")
    # print(tree.find(".//filename").text)
    # names = tree.findall(".//name")

    # for name in names:
    # 	if name.text == "pistol":
    # 		print("OK")
    # 	else:
    # 		name.text = "not-pistol"
    # 		print(name.text)

    output_name = "./pistol_not-pistol/" + tree.find('.//filename').text + " "

    obj = tree.findall(".//object")

    for ob in obj:
    	for box in ob.findall("bndbox"):

    		# print(box.find("xmin").text)
    		output_name += box.find("xmin").text + ","
    		# print(box.find("xmax").text)
    		output_name += box.find("xmax").text + ","
    		# print(box.find("ymin").text)
    		output_name += box.find("ymin").text + ","
    		# print(box.find("ymax").text)
    		output_name += box.find("ymax").text + ","

    	if ob.find(".//name").text == "pistol":
    		# print("0")
    		output_name += "0 "
    	elif ob.find(".//name").text == "not-pistol":
            continue
    		# print("1")
    		output_name += "1 "

    output_name = output_name[: -1]
    print(output_name)
    output_list.append(output_name)

    # update xml file
    tree.write(path)

print("+-------+")
print("| START |")
print("+-------+\n")

path = "C:\\Users\\junaid\\Anaconda3\\envs\\tensorflow-obj\\models\\research\\object_detection\\images\\test\\"
os.chdir(path)

for filename in os.listdir('.'):
    if filename.endswith(".xml"):
        update_xml(os.path.join(path, filename), filename)

create_output_file()

print("\n+------+")
print("| DONE |")
print("+------+")