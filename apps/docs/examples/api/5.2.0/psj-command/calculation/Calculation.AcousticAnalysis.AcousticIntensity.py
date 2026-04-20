# Title:   Calculation.AcousticAnalysis.AcousticIntensity()
# Desc:    Create the intensity from the sound pressure and particle velocity results
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/calculation/Calculation.AcousticAnalysis.AcousticIntensity
# ---
# Please set path to your sample Nastran Vibro-Acoustic file.
filePath="C:/Temp/Sample.op2"

# Prepare result model
Home.ImportResults.Nastran(strPath=filePath, dFaceAngle=60.16, dEdgeAngle=60.16, bIsVibro=True)

# AcousticAnalysis.AcousticIntensity
Calculation.AcousticAnalysis.AcousticIntensity(strName="Subcase 201")  # [hl]
