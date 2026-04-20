# Title:   Calculation.StrainGauge.ExistingResult()
# Desc:    Obtain the strain in the vector direction of the existing result
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/calculation/Calculation.StrainGauge.ExistingResult
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
                strResultName="Stress", 
                strResultCompName="XY", 
                iResultPos=4), 
                postDataOp=PostDataOp(
                iResultLocation=1, 
                iOptionCoord=1, 
                iOptionConversion=1, 
                iOptionContinuous=8))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=2, 
                    iResultSet=1, 
                    iTimeStep=2, 
                    strResultName="Stress", 
                    strResultCompName="XY"))

# StrainGauge > ExistingResult
Calculation.StrainGauge.ExistingResult(ilNodeIDs=[109], iAnalysisType=2, iResultType=6, dWidth=0.005, dLength=0.01)  # [hl]
