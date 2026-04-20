# Title:   JPT.GetResultComponentNames()
# Desc:    Get all the available result direction of the inputted result type
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetResultComponentNames
# ---
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

steps=JPT.GetResultSteps()  # [hl:start]
for step in steps:
    incs=JPT.GetResultIncrements(step.first, step.third)
    for inc in incs:
        result_comp_name = JPT.GetResultComponentNames(step.first,     # analysis type
                                                       step.third,     # result set  # [hl:end]
                                                       inc,            # time step
                                                       "Displacement", # result name
                                                       JPT.BoolType.TRUE_VAL)

        JPT.Debugger(result_comp_name)

