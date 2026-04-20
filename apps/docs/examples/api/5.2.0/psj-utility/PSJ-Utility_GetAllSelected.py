# Title:   JPT.GetAllSelected()
# Desc:    Get all the information of all selected entities (Connections, Contacts, Parts, ...)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetAllSelected
# ---
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Select part
listIDParts = [part.id for part in JPT.GetAllParts()]
strIDCursor = " ".join(str(cursor) for cursor in listIDParts)
Home.Find(strSearch=f"{strIDCursor}", strSelectedType="Part")

#Get the information of all selected parts
listSelParts = JPT.GetAllSelected()  # [hl]
JPT.Debugger(listSelParts)
