# Title:   Post.SetNote.ElementPropID()
# Desc:    Set the display of the property ID in the element's notes window
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post/Post.SetNote.ElementPropID
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

# Hide Property ID information
Post.SetNote.ElementPropID(bNoteElemPropID=False)  # [hl]
# User defines Property ID title
Post.SetNote.ElementPropID(iNoteElemPropID=1, strNoteElemPropID="Property ID")  # [hl]
