# Title:   JPT.GetResultComponentNames()
# Desc:    Get all the available result direction of the inputted result type
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_GetResultComponentNames
# ---
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

result_comp_name = JPT.GetResultComponentNames(JPT.PostAnalysisType.POST_ANALYSIS_LINEAR_STATIC,  # [hl:start]
                                               1,
                                               1,
                                               "Stress",
                                               JPT.BoolType.TRUE_VAL)  # [hl:end]

JPT.Debugger(result_comp_name)
