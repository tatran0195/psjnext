# Title:   Post.SetNote.ResultPrnVector()
# Desc:    Set the display of principal stress/principal strain unit vector in the note window
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post/Post.SetNote.ResultPrnVector
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
                strResultName="Stress", 
                strResultCompName="Max Principal Stress", 
                iResultPos=4), 
                postDataOp=PostDataOp(
                iResultLocation=1, 
                iOptionCoord=1, 
                iOptionConversion=1, 
                iOptionContinuous=8))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=2, 
                    iResultSet=1, 
                    iTimeStep=1, 
                    strResultName="Stress", 
                    strResultCompName="Max Principal Stress"))
Post.Note.Node(crlTargets=[RONode(133)])

# Hide Principal stress direction
Post.SetNote.ResultPrnVector(bNoteResultPrnVector=False)  # [hl]
# User defines Principal stress direction title
Post.SetNote.ResultPrnVector(iNoteResultPrnVector=1, strNoteResultPrnVector="Direction")  # [hl]
