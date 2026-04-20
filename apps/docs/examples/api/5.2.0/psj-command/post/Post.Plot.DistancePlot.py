# Title:   Post.Plot.DistancePlot()
# Desc:    Display the distance between two nodes in multiple steps as a step or time history graph
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post/Post.Plot.DistancePlot
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
Post.Plot.DistancePlot(crFirstNode=Node(127), crSecondNode=Node(133),   # [hl:start]
                        listPostStepItem=[
                        POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=1), 
                        POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=2), 
                        POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=3), 
                        POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=4), 
                        POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=5)], 
                        bDistanceXYZ=True)  # [hl:end]
JPT.SetActiveDocumentByName("103_solid",1)

# Distance Plot (X,Y,Z Position Plot)
Post.Plot.DistancePlot(crFirstNode=Node(127), crSecondNode=Node(133),   # [hl:start]
                        listPostStepItem=[
                        POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=1), 
                        POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=2), 
                        POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=3), 
                        POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=4), 
                        POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=5)], 
                        bPositionXYZ=True)  # [hl:end]
