# Title:   JPT.GetMaxResultId()
# Desc:    Get the ID of the node/element having the maximum value of the plotting result
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_GetMaxResultId
# ---
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

JPT.Exec('CmdShowPostContour(183:1, {1, 1, 1, Stress, XY, 4}, {1, 1, 0, 0, 1, 8, \
                             0, 0.000000, 0}, 0, {0, 0, 0, , , 0}, {0, 0, 0, 0, 0, \
                             0, 0, 0.000000, 0}, 0, {0, 0, 0, , , 0}, {0, 0, 0, 0, \
                             0, 0, 0, 0.000000, 0}, 0, 0)')

# Get the ID of the node having the maximum value of the plotting result
maxNodeID = JPT.GetMaxResultId()  # [hl]
JPT.Debugger(maxNodeID)

# Get the ID of the element having the maximum value of the plotting result
JPT.Exec('CmdShowPostContour(183:1, {1, 1, 1, Stress, XY, 2}, {2, 1, 0, 0, 0, 0, \
                             0, 0.000000, 0}, 0, {0, 0, 0, , , 0}, {0, 0, 0, 0, 0, \
                             0, 0, 0.000000, 0}, 0, {0, 0, 0, , , 0}, {0, 0, 0, 0, \
                             0, 0, 0, 0.000000, 0}, 0, 0)')

maxElemID = JPT.GetMaxResultId()  # [hl]
JPT.Debugger(maxElemID)
