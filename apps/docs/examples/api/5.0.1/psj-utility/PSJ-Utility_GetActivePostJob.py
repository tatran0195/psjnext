# Title:   JPT.GetActivePostJob()
# Desc:    Get information of active Post Job
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_GetActivePostJob
# ---
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

post_job = JPT.GetActivePostJob()  # [hl]
JPT.Debugger(post_job)
