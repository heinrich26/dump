import json
import os
import sys

def create_colored_child(filepath):
	colors = ['black','blue','brown','cyan','gray','green','light_blue','lime','magenta','orange','pink','purple','red','silver','white','yellow']
	replace = ""
	try:
		if ".json" == filepath[-5:]:
			pos = len(filepath) - 5			
			while pos >= 8:
				if filepath[pos-8:pos] == "\\models\\":
					mc_path = filepath[pos:-5]
					pos1 = len(mc_path)-1
					while pos1 != 0:
						if mc_path[pos1] == "\\":
							filename = mc_path[pos1+1:]
							rep_pos = len(filepath) - (5 + len(filename))
							pos1 = 0
						else:
							pos1 = pos1 - 1
					pos2 = pos - 9
					while pos2 != 8:
						if filepath[pos2] == "\\":
							mc_path = filepath[pos2+1:pos-8] + ":" + mc_path.replace("\\","/")
							pos = 6
							pos2 = 8
						else:
							pos2 = pos2 - 1
				elif pos == 8:
					print(valid)
				else:
					pos = pos - 1
			data = json.loads(open(filepath, "r").read())
			for x in data["textures"]:
				if "#wool" in data["textures"][x]: 
					valid = True
		print("File is valid:", valid)
	except NameError:
		input("Invalid file, press ENTER to continue")	
		exit()

	for x in colors:
		try:
			colored_path = filepath[0:rep_pos] + x + "_" + filepath[rep_pos:]
			colored_child = open(filepath[0:rep_pos] + x + "_" + filepath[rep_pos:], "x")
			colored_child.write("{\n    \"parent\": \"" + mc_path + "\",\n    \"textures\": {\n        \"wool\": \"blocks/wool_colored_" + x + "\"\n    }\n}")
			colored_child.close()
		except:
			if replace != "replace_all":
				print("The file \"" + x + "_" + filename + ".json\" already exists, press ENTER to continue, type \"replace\" to override or \"replace_all\" to override all conficts:")
				replace = input().lower()
			if replace == "replace" or "replace_all":
				colored_rep_child = open(filepath[0:rep_pos] + x + "_" + filepath[rep_pos:], "w")
				colored_rep_child.write("{\n    \"parent\": \"" + mc_path + "\",\n    \"textures\": {\n        \"wool\": \"blocks/wool_colored_" + x + "\"\n    }\n}")
				colored_rep_child.close()

try:
	create_colored_child(sys.argv[1])
except:
	import tkinter as tk
	from tkinter import filedialog

	root = tk.Tk()
	root.withdraw()

	files = filedialog.askopenfilenames(title='Choose file(s)')
	for x in files:
		create_colored_child(x.replace("/","\\"))

