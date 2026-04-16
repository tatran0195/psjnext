# Title:   JPT.MacroTCursorPairToDItemPair()
# Desc:    Convert cursor pair (Macro string type) to a pair of DItem object
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_MacroTCursorPairToDItemPair
# ---
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=7730934)
JPT.ViewFitToModel()

# Get all the information of the 2 created cubes
dItemPair = JPT.Debugger(JPT.MacroTCursorPairToDItemPair("3:1-3:2"))  # [hl]
JPT.Debugger(dItemPair.firstDItem)
JPT.Debugger(dItemPair.secondDItem)
