# Title:   JPT.GetActiveDataOption()
# Desc:    Get the active Post Data Option of the working result
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_GetActiveDataOption
# ---
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

default_result_option = \
    JPT.GetDefaultResultOption(JPT.PostAnalysisType.POST_ANALYSIS_LINEAR_STATIC,
                               1,
                               1,
                               "Stress",
                               "XX",
                               JPT.PostResultDataLoc.POST_LOC_ON_ELEMENT_NODE)

JPT.Exec('CmdShowPostContour(183:1, {1, 1, 1, Stress, XX, 2}, {1, 1, 0, 0, 16, 0, \
                             0, 0.000000, 0}, 0, {0, 0, 0, , , 0}, {0, 0, 0, 0, 0, \
                             0, 0, 0.000000, 0}, 0, {0, 0, 0, , , 0}, {0, 0, 0, 0, \
                             0, 0, 0, 0.000000, 0}, 0, 0)')

active_result_option = JPT.GetActiveDataOption()  # [hl]
JPT.Debugger(default_result_option)
JPT.Debugger(active_result_option)
