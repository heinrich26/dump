import os
import sys

def create_item_child(input_file):
	if input_file[-5:] != ".json":
		input("Invalid Filetype, press ENTER to continue!")
		exit()		
	filepath = ""
	filename = ""
	itempath = ""
	mc_path = ""
	mc_path_bs = ""
	pos = len(input_file) - 1

	while input_file[pos] != "\\":
		pos = pos - 1
	filename = input_file[(pos+1):len(input_file)]
	filepath = input_file[0:pos+1]

	pos = len(filepath)
	while pos >= 8:
		if filepath[pos-7:pos] == "\\block\\":
			itempath = filepath[0:(pos-6)] + "item\\" + filepath[(pos):len(filepath)]
			pos2 = pos - 15
			while filepath[pos2] != "\\":
				mc_path_bs = filepath[pos2] + mc_path_bs
				pos2 = pos2 - 1
			mc_path_bs = mc_path_bs + ":" + filepath[pos-6:len(filepath)]
			for i in range(0,len(mc_path_bs)):
				if '\\'!=mc_path_bs[i]:
					mc_path = mc_path + mc_path_bs[i]
				else:
					mc_path = mc_path + '/'
			pos=7
		else:
			pos = pos - 1
	if pos == 8:
		exit()

	itempath_full = itempath + filename
	try:
		os.makedirs(itempath)
	except:
		print("Directory already exists... skipping folder creation!")
		
	try:
		item_child = open(itempath_full, "x")
		item_child.write("{\n    \"parent\": \"" + mc_path + filename[0:len(filename)-5] + "\"\n}")
		item_child.close()
		print("Child model sucessfully created!")
	except:
		input("The file already exsists! Press ENTER to continue")
		exit()

try:
	create_item_child(sys.argv[1])
except:
	import tkinter as tk
	from tkinter import filedialog

	root = tk.Tk()
	root.withdraw()

	files = filedialog.askopenfilenames(title='Choose file(s)')
	for x in files:
		create_item_child(x.replace("/","\\"))
