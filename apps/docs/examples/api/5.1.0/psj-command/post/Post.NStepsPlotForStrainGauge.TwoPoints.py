# Title:   Post.NStepsPlotForStrainGauge.TwoPoints()
# Desc:    Display a graph of the stress/strain in the direction of two points
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post/Post.NStepsPlotForStrainGauge.TwoPoints
# ---
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Plot the result
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                iAnalysisType=2, 
                iResultSet=1, 
                iTimeStep=2, 
                strResultName="Strain", 
                strResultCompName="Solid Max Principal Strain", 
                iResultPos=4), 
                postDataOp=PostDataOp(iResultLocation=1, 
                iOptionCoord=1, 
                iOptionConversion=1, 
                iOptionContinuous=8))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=2, 
                    iResultSet=1, 
                    iTimeStep=2,
                    strResultName="Strain", 
                    strResultCompName="Solid Max Principal Strain"))

# NStepsPlotForStrainGauge > TwoPoints (2Nodes)
plotChart = Post.NStepsPlotForStrainGauge.TwoPoints(  # [hl:start]
            crPostJob=TSVPostJob(1), 
            crFirstNode=Node(113), 
            crSecondNode=Node(115), 
            listPostStepItem=[
                POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=1), 
                POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=2), 
                POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=3), 
                POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=4), 
                POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=5)], 
                strXAxisType="Time/Freq(Default)", 
                strYAxisType="Stress(Node)", 
            dLength=0.002, 
            dWidth=0.005, 
            iPhaseType=-1)  # [hl:end]
JPT.Debugger(plotChart)

# NStepsPlotForStrainGauge > TwoPoints (Node-Point)
plotChart = Post.NStepsPlotForStrainGauge.TwoPoints(  # [hl:start]
            crPostJob=TSVPostJob(1), 
            crFirstNode=Node(113), 
            dlPosition=[0.0176052, 0.00855172, 0.00343833], 
            listPostStepItem=[
                POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=1), 
                POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=2), 
                POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=3), 
                POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=4), 
                POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=5)], 
                strXAxisType="Time/Freq(Default)", 
                strYAxisType="Stress(Node)", 
            dLength=0.002, 
            dWidth=0.005, 
            iPhaseType=-1)  # [hl:end]
JPT.Debugger(plotChart)
