# Title:   JPT.GetActiveDocument()
# Desc:    Get information of active document
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetActiveDocument
# ---
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
Home.ImportResults.Nastran(strPath=samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
# Get information of active document
doc = JPT.GetActiveDocument()  # [hl]
JPT.Debugger(doc)
