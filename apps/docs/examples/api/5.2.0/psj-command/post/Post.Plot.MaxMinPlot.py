# Title:   Post.Plot.MaxMinPlot()
# Desc:    Display the maximum/minimum values in multiple steps on the graph in steps or time history
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post/Post.Plot.MaxMinPlot
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
Post.Plot.MaxMinPlot(listPostStepItem=[  # [hl:start]
                    POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=1), 
                    POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=2), 
                    POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=3), \
                    POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=4), 
                    POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=5)], 
                    bExportCSV=False)  # [hl:end]
