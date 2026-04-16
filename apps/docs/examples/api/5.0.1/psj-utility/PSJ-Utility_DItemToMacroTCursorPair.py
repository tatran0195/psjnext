# Title:   JPT.DItemToMacroTCursorPair()
# Desc:    Convert pair of DItem objects to Cursor pair (Macro string type)
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_DItemToMacroTCursorPair
# ---
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Get all the existing Nodes and convert a pair of them to cursor pair (Macro string type)
## Get all Nodes from model
listNodes = JPT.GetAllNodes() # List of DNode objects
## Get 2 Nodes and convert them to DItem object
dItemNode1 = JPT.CastToDItem(listNodes[0]) # The first DItem object
dItemNode2 = JPT.CastToDItem(listNodes[1]) # The second DItem object
## Return 2 DItems to a string object, for example, return value = 10:772-10:251
JPT.Debugger(JPT.DItemToMacroTCursorPair(dItemNode1, dItemNode2))  # [hl]
