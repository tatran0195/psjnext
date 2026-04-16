# Title:   JPT.GetMinResultId()
# Desc:    Get the ID of the node/element having the minimum value of the plotting result
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetMinResultId
# ---
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, XY, 4}, {1, 1, 0, 0, 1, 8, \
                             0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, \
                             0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, \
                             0, 0, 0, 0.000000, 0}, 0, 0)')

# Get the ID of the node having the minimum value of the plotting result
minNodeID = JPT.GetMinResultId()  # [hl]
JPT.Debugger(minNodeID)

# Get the ID of the element having the minimum value of the plotting result
JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, XY, 2}, {2, 1, 0, 0, 0, 0, \
                             0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, \
                             0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, \
                             0, 0, 0, 0.000000, 0}, 0, 0)')

minElemID = JPT.GetMinResultId()  # [hl]
JPT.Debugger(minElemID)
