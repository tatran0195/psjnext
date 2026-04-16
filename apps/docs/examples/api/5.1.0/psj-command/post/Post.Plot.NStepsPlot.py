# Title:   Post.Plot.NStepsPlot()
# Desc:    Get results within multiple subcases for a particular node/element/arbitrary point and plot the graph by steps or time history
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post/Post.Plot.NStepsPlot
# ---
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
# Plot the result
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                iAnalysisType=2, 
                iResultSet=1, 
                iTimeStep=1, 
                strResultName="Displacement", 
                strResultCompName="Translational", 
                iResultPos=1), 
                postDataOp=PostDataOp(
                iResultLocation=1, 
                iOptionCoord=4))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=2, 
                    iResultSet=1, 
                    iTimeStep=1, 
                    strResultName="Displacement", 
                    strResultCompName="Translational"))

# Distance Plot (X,Y,Z Distance Plot)
Post.Plot.NStepsPlot(crPostJob=TSVPostJob(1), crlTargets=[Node(133)], listPostStepItem=[  # [hl:start]
                    POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=1), 
                    POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=2), 
                    POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=3), 
                    POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=4), 
                    POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=5)], 
                    strXResult="Displacement", 
                    strXComponent="Translational", 
                    iDataLocation=1)  # [hl:end]
