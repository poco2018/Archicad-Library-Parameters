# Archicad-Library-Parameters
Python Script dumps Library Object parameters
The AddOn PlanDump.apx will place a test menu in your plan in which you can dump most of the plan's object parameters and atributes. The info is dumped in a Plan Dump.txt file which will be located in your temperary folder. This file is deleted when archicad exits so be sure to copy it to another location if you want to save it.
The info contained is quite extensive so I make up a Python script and Conmmand handler interface which will just dump a selected object's info.Add both addons - Plandump.apx and data_access.apx in your add on folder. Select a object and execute the supplied Python code. All the parameters for the object selected will print out in your script and the temp txt file.
