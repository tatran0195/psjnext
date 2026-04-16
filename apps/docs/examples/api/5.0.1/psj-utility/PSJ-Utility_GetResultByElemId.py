# Title:   JPT.GetResultByElemId()
# Desc:    Get the result value of specified Element by ID
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_GetResultByElemId
# ---
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

JPT.Exec('CmdShowPostContour(183:1, {1, 1, 1, Stress, XX, 2}, {2, 1, 0, 0, 0, 0, 0, \
                            0.000000, 0}, 0, {0, 0, 0, , , 0, 0}, {0, 0, 0, 0, 0, 0, \
                            0.000000, 0}, 0, {0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, \
                            0.000000, 0}, 0, 0)')

# Get the result value of Element ID = 658
valueElementID = JPT.GetResultByElemId(658)  # [hl]
print("Stress of XX component of Element ID = 658: " + str(valueElementID))
