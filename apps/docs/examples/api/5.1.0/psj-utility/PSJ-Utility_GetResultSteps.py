# Title:   JPT.GetResultSteps()
# Desc:    Get all the existing result types and their time steps of the current result
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetResultSteps
# ---
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

result_types_steps = JPT.GetResultSteps()  # [hl]

print("Result type: " + str(result_types_steps[0].first)) #2: JPT.PostAnalysisType.POST_ANALYSIS_MODAL
print("Result ID: " + str(result_types_steps[0].second))
print("Result step: " + str(result_types_steps[0].third))
