# Title:   JPT.GetSelectedParts()
# Desc:    Get all information of the selected parts
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_GetSelectedParts
# ---
# Prepare model
Geometry.Part.Cube(iPartColor=7138156)
Geometry.Part.Cube(strName="Cube_2", iPartColor=5921475)
Geometry.Part.Cube(strName="Cube_3", iPartColor=6678117)
Geometry.Part.Cube(strName="Cube_4", iPartColor=11908427)
Geometry.Part.Cube(strName="Cube_5", iPartColor=15429611)
Geometry.Part.Cube(strName="Cube_6", iPartColor=7531634)
Geometry.Part.Cube(strName="Cube_7", iPartColor=12434775)
Home.Find(strSearch="5 6 7 8", strSelectedType="Part")
JPT.ViewFitToModel()

# Get the information of all selected parts
listSelParts = JPT.GetSelectedParts()  # [hl]
JPT.Debugger(listSelParts)
JPT.Debugger(listSelParts[2])
