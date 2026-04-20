# Title:   JPT.DItemToMacroTCursor()
# Desc:    Convert DItem object to Cursor (Macro string type)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_DItemToMacroTCursor
# ---
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Get all the existing Nodes and convert one of them to List of Cursor (Macro string type)
## Get all Nodes from model
listNodes = [JPT.CastToDItem(node) for node in JPT.GetAllNodes()] # List of DItem objects
## Get 1 Node from the created list
node = listNodes[0] # DItem object
## Return Node to a string object, for example, return value = 10:772
JPT.Debugger(JPT.DItemToMacroTCursor(node))  # [hl]
