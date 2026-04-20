# Title:   JPT.GetAllResultsByNodeId()
# Desc:    Get all result values of specified Node by ID
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetAllResultsByNodeId
# ---
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, XX, 4}, \
                            {1, 1, 0, 0, 16, 0, 0, 0.000000, 0}, 0, \
                            {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, \
                            {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, 0)')

# Get the result values of Node ID = 60
valuesNodeID = JPT.GetAllResultsByNodeId(60)  # [hl]
for data in valuesNodeID:
    type, id, value= data
    print(f'Type:{type} ID:{id} Value:{value}')
