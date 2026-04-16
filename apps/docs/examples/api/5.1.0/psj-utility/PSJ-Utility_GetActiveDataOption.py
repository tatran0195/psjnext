# Title:   JPT.GetActiveDataOption()
# Desc:    Get the active Post Data Option of the working result
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetActiveDataOption
# ---
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
Home.ImportResults.Nastran(strPath=samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

default_result_option = \
    JPT.GetDefaultResultOption(JPT.PostAnalysisType.POST_ANALYSIS_LINEAR_STATIC,
                               1,
                               1,
                               "Stress",
                               "XX",
                               JPT.PostResultDataLoc.POST_LOC_ON_ELEMENT_NODE)

JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, XX, 2}, {1, 1, 0, 0, 16, 0, \
                             0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, \
                             0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, \
                             0, 0, 0, 0.000000, 0}, 0, 0)')

active_result_option = JPT.GetActiveDataOption()
JPT.Debugger(default_result_option)  # [hl]
JPT.Debugger(active_result_option)
