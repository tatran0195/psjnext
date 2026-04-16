# Title:   JPT.GetResultByNodeId()
# Desc:    Get the result value of specified Node by ID
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_GetResultByNodeId
# ---
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

JPT.Exec('CmdShowPostContour(183:1, {1, 1, 1, Displacement, X, 1}, {1, 1, 0, \
                            0, 0, 0, 0, 0.000000, 0}, 0, {0, 0, 0, , , 0, 0}, \
                            {0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, {0, 0, 0, , , 0}, \
                            {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, 0)')

# Get the result value of Node ID = 62
valueNodeID = JPT.GetResultByNodeId(62)  # [hl]
print("Displacement of X component of Node ID = 62: " + str(valueNodeID))
