# Title:   Post.SetNote.ResultDisp()
# Desc:    Set the display of displacement result in the note window
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post/Post.SetNote.ResultDisp
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
                strResultCompName="Mises", 
                iResultPos=2), 
                postDataOp=PostDataOp(iResultLocation=2))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=2, 
                    iResultSet=1, 
                    iTimeStep=1, 
                    strResultName="Stress", 
                    strResultCompName="Mises"))
Post.Note.Element(crlTargets=[ROElem(448)])

# Hide Displacement result information
Post.SetNote.ResultDisp(bNoteResultDisp=False)  # [hl]
# User defines Displacement result title
Post.SetNote.ResultDisp(iNoteResultDisp=1, strNoteResultDisp="Displacement")  # [hl]
