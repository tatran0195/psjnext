# Title:   JPT.GetPostElemFromPosition()
# Desc:    Get Post Element from Position
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetPostElemFromPosition
# ---
JPT.ClearLog()
# Set up model path
JupiterPath = JPT.GetAppPathInfo(JPT.PathType.PROGRAM_PATH)
modelPath = JupiterPath + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"

# Import result
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 1, 1, 1)'.format(modelPath))
JPT.ViewFitToModel()

# Show Result
JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, Mises, 2}, {2, 0, 0, 0, 0, 0, 0, 0.000000, 0}, \
0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, \
{0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, 0)')
JPT.Exec('CmdShowPostDeformation(183:1, 1, 0, 1, 1, 0, 0.000000, 0, 0.070000, 0, 0.070000, 0.070000, 0.070000, 0)')
  # [hl]
# Get Element by position
elemWith_Tolerance = JPT.GetPostElemFromPosition(16, 20, 5, 0.1, 1)
JPT.Debugger(elemWith_Tolerance) #Element ID = 409
