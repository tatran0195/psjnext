# Title:   Calculation.AcousticAnalysis.ACCombinedAnimation()
# Desc:    Perform the animation with physical quantities that select deformation, contour color, and vector separately
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/calculation/Calculation.AcousticAnalysis.ACCombinedAnimation
# ---
# Please set path to your sample Nastran Vibro-Acoustic file.
filePath="C:/Temp/Sample.op2"

# Prepare result model
Home.ImportResults.Nastran(strPath=filePath, dFaceAngle=60.16, dEdgeAngle=60.16, bIsVibro=True)

# AcousticAnalysis.ACCombinedAnimation
Calculation.AcousticAnalysis.ACCombinedAnimation(iTimeStep=2, iAnalysisType=4, strName="Subcase 201")  # [hl]
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                iAnalysisType=4, 
                iResultSet=201, 
                iTimeStep=2, 
                strResultName="Fluid Pressure", 
                strResultCompName="P", 
                iResultPos=1), 
                postDataOp=PostDataOp(
                iResultLocation=1, 
                iOptionCoord=1, 
                iOptionComplex=16))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=4, 
                    iResultSet=201, 
                    iTimeStep=2, 
                    strResultName="Fluid Pressure", 
                    strResultCompName="P"), 
                    postDataOption=PostDataOp(iOptionComplex=16))
