# Title:   Tools.ToPre()
# Desc:    Convert the model’s data and the related settings from an opening Post document to a new Pre document. All part names, setting item names and data of setting items in the model are preserved during conversion
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post-tools/Tools.ToPre
# ---
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\Post\\Static_Renkon.op2"
Home.ImportResults.Nastran(strPath= samplePath, dFaceAngle=60.16, dEdgeAngle=60.16, bReadLoadAndConstraint=True, 
                            bReadConnection=True, bCreateResultsAtMidNode=True)
# Convert to Pre
data = Tools.ToPre(strName="Static_Renkon", ilOptions=[0, 1, 2, 3, 4])  # [hl]
JPT.SetActiveDocumentByName("Static_Renkon",1)
JPT.Debugger(data)
