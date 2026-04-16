# Title:   JPT.CastDItemToDROElem()
# Desc:    Convert DItem object to DPostElem object
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_CastDItemToDROElem
# ---
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

# Get Element object as DItem object from the created list of DItem objects
listDItemPostElems = JPT.GetAllByTypeID(JPT.DItemType.POST_ELEM)
dItemPostElem = listDItemPostElems[0]
JPT.Debugger(dItemPostElem)

# Convert from the above DItem object to DElem object
dPostElem = JPT.CastDItemToDROElem(dItemPostElem)  # [hl]
JPT.Debugger(dPostElem)
