# Title:   JPT.GetDocumentList()
# Desc:    Get information of all displaying documents
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetDocumentList
# ---
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
Home.ImportResults.Nastran(strPath=samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
JPT.CreateNewDocument()
# Get information of all displaying documents
docList = JPT.GetDocumentList()  # [hl]
for doc in docList:
    JPT.Debugger(doc)
