# Title:   JPT.GetAllPartsInSubAssembly()
# Desc:    Get all the information of all parts under the inputted sub-assembly
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetAllPartsInSubAssembly
# ---
# Prepare model
Geometry.Part.Cube(iPartColor=15426917)
Geometry.Part.Cube(strName="Cube_2", iPartColor=13390932)
Geometry.Part.Cube(strName="Cube_3", iPartColor=16448103)
Geometry.Part.Cube(strName="Cube_4", iPartColor=13619046)
Geometry.Part.Cube(strName="Cube_5", iPartColor=7861111)
JPT.ViewFitToModel()
Assembly.RightClick.AddSubAssembly()

# Copy all parts to the created Subassembly
currentDoc = JPT.GetActiveDocument()
Assembly.RightClick.TransferDocumentData(strSourceDocTitle=currentDoc.docName, 
                                        strDestDocTitle=currentDoc.docName, 
                                        crlParts=[Part(part.id) for part in JPT.GetAllParts()], 
                                        strlNewPartName=[], 
                                        crDestAssemblyInstance=Inst(1))  # [hl]

# Get the information of all parts belonging to the inputted sub-assembly
listPartsInSubAssembly = JPT.GetAllPartsInSubAssembly(JPT.FindSubAssemblyByID(1))
JPT.Debugger(listPartsInSubAssembly)
