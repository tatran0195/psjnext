# Title:   Post.Note.ElementSearchFromPoints()
# Desc:    Search the nearest element from the specified point and markup its element note
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post/Post.Note.ElementSearchFromPoints
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

# Search elements from points and markup notes
element = Post.Note.ElementSearchFromPoints(dlPositions=[[30.0, 3.0, 2.5], [28.0, 8.0, 4.0]])  # [hl]
if len(element) >=1:
    for i in range(len(element)):
        print("The searched element is:", str(element[i]))
else:
    print("Cannot search the element from point")
