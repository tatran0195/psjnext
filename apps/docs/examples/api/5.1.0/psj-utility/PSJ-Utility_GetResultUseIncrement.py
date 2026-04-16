# Title:   JPT.GetResultUseIncrement()
# Desc:    Check whether the result having any increment or not
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetResultUseIncrement
# ---
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

is_increment_exist = \  # [hl:start]
    JPT.GetResultUseIncrement(JPT.PostAnalysisType.POST_ANALYSIS_MODAL, 1)  # [hl:end]

JPT.Debugger(is_increment_exist)
