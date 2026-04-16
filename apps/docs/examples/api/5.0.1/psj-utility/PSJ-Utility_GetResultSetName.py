# Title:   JPT.GetResultSetName()
# Desc:    Get the name of Result Set (Subcase)
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_GetResultSetName
# ---
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

result_set_name = JPT.GetResultSetName(1,1)  # [hl]
JPT.Debugger(result_set_name)
