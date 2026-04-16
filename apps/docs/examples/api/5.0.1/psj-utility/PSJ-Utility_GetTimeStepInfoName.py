# Title:   JPT.GetTimeStepInfoName()
# Desc:    Get the name of Time Step Info
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_GetTimeStepInfoName
# ---
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

time_step_info_name = JPT.GetTimeStepInfoName(2,1,1)  # [hl]
JPT.Debugger(time_step_info_name) # Mode 1, Freq=3.235953e+04
