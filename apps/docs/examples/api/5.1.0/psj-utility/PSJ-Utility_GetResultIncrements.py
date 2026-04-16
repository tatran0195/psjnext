# Title:   JPT.GetResultIncrements()
# Desc:    Get all the existing increments of the inputted result step
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetResultIncrements
# ---
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

result_increments = \  # [hl:start]
    JPT.GetResultIncrements(JPT.PostAnalysisType.POST_ANALYSIS_MODAL,
                            1)
  # [hl:end]
JPT.Debugger(result_increments)
