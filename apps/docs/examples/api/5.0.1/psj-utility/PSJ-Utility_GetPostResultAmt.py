# Title:   JPT.GetPostResultAmt()
# Desc:    Get Physical Amount information of the specify result
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_GetPostResultAmt
# ---
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, \
                               1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

amt_info = JPT.GetPostResultAmt(JPT.PostAnalysisType.POST_ANALYSIS_LINEAR_STATIC,  # [hl:start]
                               1,
                               1,
                               "Stress",
                               "XX",
                               JPT.PostResultDataLoc.POST_LOC_ON_ELEMENT_NODE)  # [hl:end]
JPT.Debugger(amt_info)
