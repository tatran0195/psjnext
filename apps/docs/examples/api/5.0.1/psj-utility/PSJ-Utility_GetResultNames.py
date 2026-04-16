# Title:   JPT.GetResultNames()
# Desc:    Get all the available result type existing on the model
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_GetResultNames
# ---
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

result_name = JPT.GetResultNames(JPT.PostAnalysisType.POST_ANALYSIS_LINEAR_STATIC,  # [hl:start]
                                 1,
                                 1,
                                 JPT.BoolType.TRUE_VAL)  # [hl:end]

JPT.Debugger(result_name)
