# Title:   JPT.GetSuppressedParts()
# Desc:    Get all information of all suppressed parts
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_GetSuppressedParts
# ---
# Prepare model
Geometry.Part.Cube(iPartColor=7138156)
Geometry.Part.Cube(strName="Cube_2", iPartColor=5921475)
Geometry.Part.Cube(strName="Cube_3", iPartColor=6678117)
Geometry.Part.Cube(strName="Cube_4", iPartColor=11908427)
Geometry.Part.Cube(strName="Cube_5", iPartColor=15429611)
Geometry.Part.Cube(strName="Cube_6", iPartColor=7531634)
Geometry.Part.Cube(strName="Cube_7", iPartColor=12434775)
Assembly.RightClick.Suppress(crlParts=[Part(3, 5, 4)])
JPT.ViewFitToModel()

# Get the information of all selected parts
listSuppressedParts = JPT.GetSuppressedParts()  # [hl]
JPT.Debugger(listSuppressedParts) #list has size = 3
JPT.Debugger(listSuppressedParts[0]) #DBody item: Cube 3
