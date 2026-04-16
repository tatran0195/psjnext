# Title:   JPT.GetResultLocations()
# Desc:    Get all the available data location existing on the inputted result type and direction
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_GetResultLocations
# ---
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

result_location = \  # [hl:start]
    JPT.GetResultLocations(JPT.PostAnalysisType.POST_ANALYSIS_LINEAR_STATIC,
                           1,
                           1,
                           "Stress",
                           "XX")  # [hl:end]

JPT.Debugger(result_location)
#2: JPT.PostResultDataLoc.POST_LOC_ON_ELEMENT
#4: JPT.PostResultDataLoc.POST_LOC_ON_ELEMENT_NODE
