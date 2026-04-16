# Title:   JPT.GetUndoCount()
# Desc:    Get the total number of undo action which is capable for executing
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_GetUndoCount
# ---
# Prepare model and undo steps
Geometry.Part.Cube(strName="Cube_11", iPartColor=11842649)
Geometry.Part.Cube(strName="Cube_12", iPartColor=14968422)
Geometry.Part.Cube(strName="Cube_13", iPartColor=6250447)
Geometry.Part.Cube(strName="Cube_14", iPartColor=12734402)
Geometry.Part.Cube(strName="Cube_15", iPartColor=16579696)
Geometry.Part.Cube(strName="Cube_16", iPartColor=7666683)
Geometry.Part.Cube(strName="Cube_17", iPartColor=12867524)

# Get the number of the available Undo
iUndoSteps = JPT.GetUndoCount()  # [hl]
JPT.Debugger(iUndoSteps) # Return an integer object with value = 7
