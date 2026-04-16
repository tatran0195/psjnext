# Title:   JPT.GetElementResult()
# Desc:    Get all elements with the loaded element results that satisfy a condition
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_GetElementResult
# ---
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

JPT.Exec('CmdShowPostContour(183:1, {1, 1, 1, Stress, Max Principal Stress, 2}, {2, 1, 0, 0, 0, 0,\
                             0, 0.000000, 0}, 0, {0, 0, 0, , , 0}, {0, 0, 0, 0, 0, \
                             0, 0, 0.000000, 0}, 0, {0, 0, 0, , , 0}, {0, 0, 0, 0, \
                             0, 0, 0, 0.000000, 0}, 0, 0)')

# Create a elemental group whose element results greater than 1 (tolerance=10E-3)
list_element_1= JPT.GetElementResult(JPT.PostDataRangeType.GT,1,10E-3)  # [hl]
Tools.Group.CreateGroup(strGroupName="Group_Element_1", crlTargets=list_element_1)

# Create a elemental group whose element results in range (1,5)
list_element_2= JPT.GetElementResult(JPT.PostDataRangeType.IR,1,5)  # [hl]
Tools.Group.CreateGroup(strGroupName="Group_Element_2", crlTargets=list_element_2)
