# Title:   Calculation.SurfaceDistance.DistanceCalculate()
# Desc:    Display the distance between parts as a contour
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/calculation/Calculation.SurfaceDistance.DistanceCalculate
# ---
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60, dEdgeAngle=60)

# Plot the displacement result
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                iAnalysisType=1, 
                iResultSet=1, 
                iTimeStep=1, 
                strResultName="Displacement", 
                strResultCompName="Translational", 
                iResultPos=1), 
                postDataOp=PostDataOp(iResultLocation=1, iOptionCoord=1))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=1, 
                    iResultSet=1, 
                    iTimeStep=1, 
                    strResultName="Displacement", 
                    strResultCompName="Translational"))
Post.EnableMiddleNodes()

# Surface distance
Calculation.SurfaceDistance.DistanceCalculate(dEdgeTolerance=2.0, crReferenceNode=Node(124), crFirstTarget=Part(4),   # [hl:start]
                                            crSecondTarget=Part(6))  # [hl:end]
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                iAnalysisType=1, 
                iAnalysisID=1, 
                iResultSet=1000, 
                strResultName="Untitled", 
                strResultCompName="SurfaceDistance", 
                iResultPos=1), 
                postDataOp=PostDataOp(iResultLocation=1, iOptionCoord=1))])
Post.EnableMiddleNodes()
