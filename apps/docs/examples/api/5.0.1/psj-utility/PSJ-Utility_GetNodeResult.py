# Title:   JPT.GetNodeResult()
# Desc:    Get all nodes with the loaded nodal results that satisfy a condition
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_GetNodeResult
# ---
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

JPT.Exec('CmdShowPostContour(183:1, {1, 1, 1, Stress, Max Principal Stress, 4}, {1, 1, 0, 0, 1, 8, \
                             0, 0.000000, 0}, 0, {0, 0, 0, , , 0}, {0, 0, 0, 0, 0, \
                             0, 0, 0.000000, 0}, 0, {0, 0, 0, , , 0}, {0, 0, 0, 0, 0, \
                             0, 0, 0.000000, 0}, 0, 0)')

# Create a nodal group whose nodal results greater than 1 (tolerance=10E-3)
list_node_1= JPT.GetNodeResult(JPT.PostDataRangeType.GT,1,10E-3)  # [hl]
Tools.Group.CreateGroup(strGroupName="Group_Node_1", crlTargets=list_node_1)

# Create a nodal group  whose nodal results in range (1,5)
list_node_2= JPT.GetNodeResult(JPT.PostDataRangeType.IR,1,5)  # [hl]
Tools.Group.CreateGroup(strGroupName="Group_Node_2", crlTargets=list_node_2)
