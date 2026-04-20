# Title:   JPT.CastDItemToDRONode()
# Desc:    Convert DItem object to DPostNode object
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_CastDItemToDRONode
# ---
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

# Get LBC object (Pressure) as DItem object from the created list of DItem objects
listDItemPostNodes = JPT.GetAllByTypeID(JPT.DItemType.POST_NODE)
dItemPostNode = listDItemPostNodes[0]
JPT.Debugger(dItemPostNode)

# Convert from the above DItem object to DPostNode object
dPostNode = JPT.CastDItemToDRONode(dItemPostNode)  # [hl]
JPT.Debugger(dPostNode)
