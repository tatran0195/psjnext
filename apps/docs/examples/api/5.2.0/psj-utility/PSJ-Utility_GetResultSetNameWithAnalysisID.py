# Title:   JPT.GetResultSetNameWithAnalysisID()
# Desc:    Get the name of Result Set (Subcase)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetResultSetNameWithAnalysisID
# ---
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

result_set_name = JPT.GetResultSetNameWithAnalysisID(1,0,1)  # [hl]
JPT.Debugger(result_set_name)
