# Title:   JPT.CloseDocumentByID()
# Desc:    Close indicated document by using its ID.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_CloseDocumentByID
# ---
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
Home.ImportResults.Nastran(strPath=samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
JPT.CreateNewDocument()
for doc in JPT.GetDocumentList():
    if doc.docName == "101_solid":
        JPT.CloseDocumentByID(doc.docID)  # [hl]
