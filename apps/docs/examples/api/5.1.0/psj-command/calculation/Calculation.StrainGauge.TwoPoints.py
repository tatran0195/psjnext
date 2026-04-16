# Title:   Calculation.StrainGauge.TwoPoints()
# Desc:    Display stress and strain in the direction connecting two points
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/calculation/Calculation.StrainGauge.TwoPoints
# ---
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Plot the result
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                iAnalysisType=2, 
                iResultSet=1, 
                iTimeStep=2, 
                strResultName="Strain", 
                strResultCompName="Solid Max Principal Strain", 
                iResultPos=4), 
                postDataOp=PostDataOp(iResultLocation=1, 
                iOptionCoord=1, 
                iOptionConversion=1, 
                iOptionContinuous=8))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=2, 
                    iResultSet=1, 
                    iTimeStep=2,
                    strResultName="Strain", 
                    strResultCompName="Solid Max Principal Strain"))

# StrainGauge > TwoPoints
Calculation.StrainGauge.TwoPoints(iNodeID=110, iNodeID2=111, dWidth=0.005, dLength=0.01)  # [hl]
