# Title:   JPT.CloseDocumentByName()
# Desc:    Close indicated document by using its name.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_CloseDocumentByName
# ---
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
Home.ImportResults.Nastran(strPath=samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
JPT.CreateNewDocument()
JPT.CloseDocumentByName("101_solid")  # [hl]
