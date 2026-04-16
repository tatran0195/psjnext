# Title:   JPT.GetPostSolverType()
# Desc:    Get the Post Job type of the current importing result
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetPostSolverType
# ---
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Get Post Job type
type = JPT.GetPostSolverType()  # [hl]
print(type)
