# Title:   JPT.SetActiveDocumentByID()
# Desc:    Set indicated document in active by using its ID
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_SetActiveDocumentByID
# ---
doc1 = JPT.CreateNewDocument()
doc2 = JPT.CreateNewDocument()
JPT.SetActiveDocumentByID(doc1.docID, 1)  # [hl]
Geometry.Part.Cube()
JPT.ViewFitToModel()
