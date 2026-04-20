# Title:   JPT.GetAllPostElems()
# Desc:    Get all the information of all existing Post (read-only) elements
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetAllPostElems
# ---
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, XX, 4}, \
                            {2, 1, 0, 0, 1, 0, 0, 0.000000, 0}, 0, \
                            {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, \
                            0, {0, 0, 0, 0, , , 0}, \
                            {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, 0)')

# Get the result values of Elements
for postElem in JPT.GetAllPostElems():  # [hl]
    value=JPT.GetResultByElemId(postElem.id)
    print(f"Stress of XX component of Element ID = {postElem.id}:{value}")
