# Title:   JPT.GetResultNames()
# Desc:    Get all the available result type existing on the model
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetResultNames
# ---
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

#Get All Result Names in all steps and increments  # [hl:start]
steps=JPT.GetResultSteps()
for step in steps:
    incs=JPT.GetResultIncrements(step.first, step.third)
    for inc in incs:  # [hl:end]
        result_name = JPT.GetResultNames(step.first,    #analysis type
                                         step.third,    #result set
                                         inc,           #time step
                                         JPT.BoolType.TRUE_VAL)

        JPT.Debugger(result_name)
