# Title:   Post.SetNote.ResultPos()
# Desc:    Set the display of coordinates of the selected position in the note window
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post/Post.SetNote.ResultPos
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
Post.Note.Position(crElement=ROElem(448), dlPosition=[28.588114, 6.313289, 5.0])

# Hide Position information
Post.SetNote.ResultPos(bNoteResultPos=False)  # [hl]
# User defines Position title
Post.SetNote.ResultPos(iNoteResultPos=1, strNoteResultPos="Position")  # [hl]
