# Title:   Tools.ContourCopy()
# Desc:    Display the contour of the current Post document in the specified Pre document
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post-tools/Tools.ContourCopy
# ---
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
Home.ImportResults.Nastran(strPath= samplePath, dFaceAngle=60.16, dEdgeAngle=60.16, bReadLoadAndConstraint=True, 
                            bReadConnection=True, bCreateResultsAtMidNode=True)

# Prepare Pre model
Tools.ToPre(strName="101_solid", ilOptions=[0, 1, 2, 3, 4])
# Plot the result
JPT.SetActiveDocumentByName("101_solid",1)
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                iAnalysisType=1, 
                iResultSet=1, 
                iTimeStep=1, 
                strResultName="Displacement", 
                strResultCompName="Translational", 
                iResultPos=1), 
                postDataOp=PostDataOp(
                iResultLocation=1, 
                iOptionCoord=1))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=1, 
                    iResultSet=1, 
                    iTimeStep=1, 
                    strResultName="Displacement", 
                    strResultCompName="Translational"))
Post.EnableMiddleNodes()

# Copy contour
dataCopy = Tools.ContourCopy(strPostDocName="101_solid", strPreDocName="101_solid_Converted_Pre")  # [hl]
JPT.Debugger(dataCopy)
