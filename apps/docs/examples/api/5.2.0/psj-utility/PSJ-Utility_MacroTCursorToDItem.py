# Title:   JPT.MacroTCursorToDItem()
# Desc:    Convert cursor (Macro string type) to a DItem object
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_MacroTCursorToDItem
# ---
# Prepare model
Geometry.Part.Cube()
JPT.ViewFitToModel()

# Convert to DItem and get all the information of the created Cube_1
dItem = JPT.Debugger(JPT.MacroTCursorToDItem("3:1"))  # [hl]
JPT.Debugger(dItem)
