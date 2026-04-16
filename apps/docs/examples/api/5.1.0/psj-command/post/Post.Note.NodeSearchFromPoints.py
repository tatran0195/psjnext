# Title:   Post.Note.NodeSearchFromPoints()
# Desc:    Search the nearest node from the specified point and markup its node note
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post/Post.Note.NodeSearchFromPoints
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
                    
# Search nodes from points and markup notes
node = Post.Note.NodeSearchFromPoints(dlPositions=[[30.0, 3.0, 2.5], [28.0, 8.0, 4.0]])  # [hl]
if len(node) >=1:
    for i in range(len(node)):
        print("The searched node is:", str(node[i]))
else:
    print("Cannot search the node from point")
