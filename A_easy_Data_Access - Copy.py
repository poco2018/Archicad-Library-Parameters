from importlib import import_module
from archicad import ACConnection
import archicad
import sys

#from A_Testing import EPVArray

conn = ACConnection.connect()

assert conn, f'Communication Link is not available -timed out'

acc = conn.commands
act = conn.types
acu = conn.utilities

parameters = {}
parameters["command"] = "GetSelected"
parameters["inParams"] = ['']
response = acc.ExecuteAddOnCommand(act.AddOnCommandId('AdditionalJSONCommands','Utilities'),parameters)
out = response
guid_str = str(out['outparams2'][0][0])
parameters["command"] = "GetLibraryParameters"
parameters["inParams"] = [guid_str]
response = acc.ExecuteAddOnCommand(act.AddOnCommandId('AdditionalJSONCommands','LibraryParams'),parameters)
for value in response['outparams2']:
  print(value)
sys.exit()
