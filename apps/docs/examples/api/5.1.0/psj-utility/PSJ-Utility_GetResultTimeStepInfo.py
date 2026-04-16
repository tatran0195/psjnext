# Title:   JPT.GetResultTimeStepInfo()
# Desc:    Get the relating information of the inputted result step with it's time step
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetResultTimeStepInfo
# ---
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

result_time_step_info = JPT.GetResultTimeStepInfo(JPT.PostAnalysisType.POST_ANALYSIS_MODAL,  # [hl:start]
                                           1,
                                           10)
  # [hl:end]
JPT.Debugger(result_time_step_info)

print(result_time_step_info.mode)
print(result_time_step_info.time)
print(result_time_step_info.freq)
