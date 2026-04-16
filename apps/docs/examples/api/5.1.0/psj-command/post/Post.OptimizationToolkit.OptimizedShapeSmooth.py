# Title:   Post.OptimizationToolkit.OptimizedShapeSmooth()
# Desc:    Create iso-surfaces (smoothing) based on nodal density and element density within optimization results, and convert them into a mesh.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post/Post.OptimizationToolkit.OptimizedShapeSmooth
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

# Set appropriate values
Post.OptimizationToolkit.OptimizedShapeSmooth(  # [hl:start]
    crlDesignedParts=[Part(1)], 
    dDensityRatio=0.75, 
    bKeepSharedNodeOnBody=True, 
    dMeshSize=0.002845)  # [hl:end]
