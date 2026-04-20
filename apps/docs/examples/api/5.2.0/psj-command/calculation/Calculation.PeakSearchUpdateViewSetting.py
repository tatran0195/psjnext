# Title:   Calculation.PeakSearchUpdateViewSetting()
# Desc:    Update the view setting of peak search
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/calculation/Calculation.PeakSearchUpdateViewSetting
# ---
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\Post\\Static_Renkon.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
# Plot the result
Post.ShowContour(
  crPostJob=TSVPostJob(1),
   lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
    iAnalysisType=1, 
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
Post.ShowDeformation(
  crPostJob=TSVPostJob(1), 
  postResultKey=PostResultKey(
    iAnalysisType=1, 
    iResultSet=1, 
    iTimeStep=1, 
    strResultName="Stress", 
    strResultCompName="Max Principal Stress"))

# Peak search and update view settings
Calculation.PeakSearch(bStep=False, crlTargets=[Part(1)])
view_setting = Calculation.PeakSearchUpdateViewSetting(  # [hl:start]
  bFlagVisibleAreaOnly=True, 
  bVectorMaxPrincipalStress=True, 
  bFlagColor=True)  # [hl:end]
print(view_setting)
