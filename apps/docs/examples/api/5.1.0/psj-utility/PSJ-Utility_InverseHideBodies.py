# Title:   JPT.InverseHideBodies()
# Desc:    Show the part having the inputted ID only
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_InverseHideBodies
# ---
# Prepare model
Geometry.Part.Cube(strName="Cube_11", iPartColor=11842649)
Geometry.Part.Cube(strName="Cube_12", iPartColor=14968422)
Geometry.Part.Cube(strName="Cube_13", iPartColor=6250447)
Geometry.Part.Cube(strName="Cube_14", iPartColor=12734402)
Geometry.Part.Cube(strName="Cube_15", iPartColor=16579696)

# Show the part with ID = 3 only (Cube_13)
selAllParts = JPT.GetAllParts()
showPart = selAllParts[2].id
JPT.Debugger(selAllParts[2])
JPT.InverseHideBodies(showPart)  # [hl]
