# Title:   Home.RectangularCapture.Multiple()
# Desc:    Create a frame for Multiple capture and save it in the “User Frame” tree of the ViewPoint window. The created frame will be used with the "To PPT" and "To Image" command
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/home/Home.RectangularCapture.Multiple
# ---
# Prepare model
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

# Create a multiple frames
Home.RectangularCapture.Multiple(strFrameName="New_Frame_1 ((Multiple))", iStartPointX=459, iStartPointY=212,   # [hl:start]
                                iWidth=460, iHeight=214)  # [hl:end]
Home.ToPPTX()
