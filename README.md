# dump
Python Ressource Tweaks: 
  my python scripts to automate Minecraft modeling workflows
  Create_Item_Child: creates a child model for a block model within the correct folder structure!
  it is required, that your folders match the MC folderstructure: assets/own_namespace/models/block/your_files.json ! If theres more folder structurel,
  it will be replicated in the models/item folder. The Created model references the file, the script was ran on. 
  Create_Colored_Models: creates child models for every wool color in the same folder, that reference the file, the script was referenced to and adds the texture "wool" which
  has their texture. The parent model must have a texture with the value #wool
  
  Usage:
  Either execute the programm with python from console/double click and chose a file or multiple files or right click any json file in the explorer and use the action 
  added by the script.
  
  Installation: (Windows only)
  Python 3 required
  The script adds a context menu to the explorer, the .py scripts can be used without installation
  unpack the .zip File and execute the "install.bat" as admin, because this adds a button to your explorer menu. If you dont want a explorer button, dont use the script!
  The "uninstall.bat" will remove the folder and your Explorer context menu entry.
  You must have set python to the PATH environment variable (so you can just type python in the console to run python instead of typing C:\Windows\py.exe), if not, you can change
  the explorer entry by hand from py.exe to C\Windows\py.exe (or where you have installed it) by opening Win + R, type "regedit" and navigate to
  "HKEY_CLASSES_ROOT\*\shell\CreateColoredModels\command" and "CreateItemModel\command" and edit the value of (Default). You must run the script first.
