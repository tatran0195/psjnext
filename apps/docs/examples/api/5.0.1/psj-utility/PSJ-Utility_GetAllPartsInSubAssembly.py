# Title:   JPT.GetAllPartsInSubAssembly()
# Desc:    Get all the information of all parts under the inputted sub-assembly
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_GetAllPartsInSubAssembly
# ---
# Prepare model
Geometry.Part.Cube(iPartColor=15426917)
Geometry.Part.Cube(strName="Cube_2", iPartColor=13390932)
Geometry.Part.Cube(strName="Cube_3", iPartColor=16448103)
Geometry.Part.Cube(strName="Cube_4", iPartColor=13619046)
Geometry.Part.Cube(strName="Cube_5", iPartColor=7861111)
JPT.ViewFitToModel()
Assembly.RightClick.AddSubAssembly()
listIDParts = [part.id for part in JPT.GetAllParts()]
listIDCursorParts = ["3:{}".format(id) for id in listIDParts]
strIDCursor = ", ".join(cursor for cursor in listIDCursorParts)
# Change the document name if the current Document is not "Jupiter1"
JPT.Exec(f'TransferDocumentData("Jupiter1", "Jupiter1", [{strIDCursor}], [], 2:1, 0)')

# Get the information of all parts belonging to the inputted sub-assembly
listPartsInSubAssembly = JPT.GetAllPartsInSubAssembly(JPT.FindSubAssemblyByID(1))  # [hl]
JPT.Debugger(listPartsInSubAssembly)
