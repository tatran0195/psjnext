# Title:   JPT.GetDocumentByName()
# Desc:    Get information of an indicated document by using its name
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetDocumentByName
# ---
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
Home.ImportResults.Nastran(strPath=samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
docInfor = JPT.GetDocumentByName("101_solid")  # [hl]
JPT.Debugger(docInfor)
