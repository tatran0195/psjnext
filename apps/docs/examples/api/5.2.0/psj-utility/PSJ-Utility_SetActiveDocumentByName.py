# Title:   JPT.SetActiveDocumentByName()
# Desc:    Set indicated document in active by using its name
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_SetActiveDocumentByName
# ---
doc1 = JPT.CreateNewDocument()
doc2 = JPT.CreateNewDocument()
doc3 = JPT.CreateNewDocument()
JPT.SetActiveDocumentByName(doc2.docName,1)  # [hl]
Geometry.Part.Cube()
JPT.ViewFitToModel()
print("Created a Cube in " + str(doc2.docName) + " document")
