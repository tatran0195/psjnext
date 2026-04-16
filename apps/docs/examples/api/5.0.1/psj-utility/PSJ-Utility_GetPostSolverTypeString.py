# Title:   JPT.GetPostSolverTypeString()
# Desc:    Get solver type of the current importing result
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_GetPostSolverTypeString
# ---
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

strSolverType = JPT.GetPostSolverTypeString()  # [hl]
JPT.Debugger(strSolverType)
