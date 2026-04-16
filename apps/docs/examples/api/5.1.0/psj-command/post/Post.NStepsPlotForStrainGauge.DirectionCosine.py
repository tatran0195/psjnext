# Title:   Post.NStepsPlotForStrainGauge.DirectionCosine()
# Desc:    Display a graph of the stress/strain in the direction cosine of the entered direction vector
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post/Post.NStepsPlotForStrainGauge.DirectionCosine
# ---
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\111_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# NStepsPlotForStrainGauge > DirectionCosine
plot = Post.NStepsPlotForStrainGauge.DirectionCosine(  # [hl:start]
    crPostJob=TSVPostJob(1), 
    crlTargets=[Node(113, 111)], 
    listPostStepItem=[
        POST_STEP_ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=1), 
        POST_STEP_ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=2), 
        POST_STEP_ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=3), 
        POST_STEP_ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=4), 
        POST_STEP_ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=5), 
        POST_STEP_ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=6), 
        POST_STEP_ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=7), 
        POST_STEP_ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=8), 
        POST_STEP_ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=9), 
        POST_STEP_ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=10)], 
    strXAxisType="Time/Freq(Default)", 
    strYAxisType="Stress(Node)", 
    dLength=0.002, 
    dWidth=0.001)  # [hl:end]
JPT.Debugger(plot)
