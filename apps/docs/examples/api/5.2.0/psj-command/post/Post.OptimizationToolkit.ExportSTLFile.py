# Title:   Post.OptimizationToolkit.ExportSTLFile()
# Desc:    Output the currently displayed shape as an .stl file based on density threshold values.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post/Post.OptimizationToolkit.ExportSTLFile
# ---
# Import arbitrary topology optimization result
Home.ImportResults.ADVC("C:/Temp/ADVCResult", iImportType=1)

Post.ShowContour(
    crPostJob=TSVPostJob(1), 
    lContourSettings=[
        PostContourSetting(postResultKey=PostResultKey(
            iAnalysisType=11, 
            iResultSet=10, 
            iTimeStep=-1, 
            strResultName="DensityRatio", 
            strResultCompName="DensityRatio", 
            iResultPos=2), 
        postDataOp=PostDataOp(iResultLocation=2, iOptionCoord=1))])
Post.OptimizationToolkit.EnableOptimizationMode()

# Set appropriate density value
Post.OptimizationToolkit.OptimizedShape(dTopologyDensity=0.75)

Post.OptimizationToolkit.ExportSTLFile(strSTLPath="C:/Temp/temp.stl")  # [hl]
