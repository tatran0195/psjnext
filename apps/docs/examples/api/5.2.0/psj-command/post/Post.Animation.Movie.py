# Title:   Post.Animation.Movie()
# Desc:    Export animation as a movie file.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post/Post.Animation.Movie
# ---
import os

samplePath = os.path.join(JPT.GetProgramPath(),r"SampleData\PSJ\PSJ-Utility\PostSample\101_solid.op2")
Home.ImportResults.Nastran(strPath=samplePath)

# Show contour
Post.ShowContour(
    crPostJob=TSVPostJob(1), 
    lContourSettings=[
        PostContourSetting(
            postResultKey=PostResultKey(
                iAnalysisType=1, iResultSet=1, iTimeStep=1, strResultName="Displacement", 
                strResultCompName="Translational", iResultPos=1), 
                postDataOp=PostDataOp(iResultLocation=1, iOptionCoord=1))])

Post.ShowDeformation(
    crPostJob=TSVPostJob(1), 
    postResultKey=PostResultKey(
        iAnalysisType=1, iResultSet=1, iTimeStep=1, strResultName="Displacement", strResultCompName="Translational"))
Post.EnableMiddleNodes()

temp_folder=JPT.GetAppPathInfo(JPT.PathType.TEMP_PATH)
outputPath = os.path.join(temp_folder,"101_solid_movie.mp4")

Post.Animation.Movie(  # [hl:start]
    strFilePath=outputPath, 
    strEncoder="h264", 
    iFPS=8, 
    iRepeat=1, 
    iWidth=882, 
    iHeight=441)  # [hl:end]
