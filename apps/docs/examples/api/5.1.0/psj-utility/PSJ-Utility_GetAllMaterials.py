# Title:   JPT.GetAllMaterials()
# Desc:    Get all the information of all existing user materials
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetAllMaterials
# ---
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\Post\\Static_Renkon.op2"
Home.ImportResults.Nastran(strPath= samplePath, dFaceAngle=60.16, dEdgeAngle=60.16, bReadLoadAndConstraint=True, 
                            bReadConnection=True, bCreateResultsAtMidNode=True)
# Convert to Pre
data = Tools.ToPre(strName="Static_Renkon", ilOptions=[0, 1, 2, 3, 4])
JPT.SetActiveDocumentByName("Static_Renkon_Converted_Pre",1)
# Get all user materials
userMat = JPT.GetAllMaterials()
JPT.Debugger(userMat)
JPT.Debugger(userMat[0])  # [hl]
