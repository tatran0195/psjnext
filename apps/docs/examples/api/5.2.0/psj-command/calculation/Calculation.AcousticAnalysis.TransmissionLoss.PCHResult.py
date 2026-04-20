# Title:   Calculation.AcousticAnalysis.TransmissionLoss.PCHResult()
# Desc:    Read a Punch file (*.pch) containing information on the coupled surfaces output from a Nastran structural-acoustic coupled calculation and create a nodal group on the acoustic model
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/calculation/Calculation.AcousticAnalysis.TransmissionLoss.PCHResult
# ---
# Please set path to your sample Nastran Vibro-Acoustic file and Punch file.
ResultFile="C:/Temp/Sample.op2"
PunchFile="C:/Temp/PunchSample.pch"

# Prepare result model
Home.ImportResults.Nastran(strPath=ResultFile, dFaceAngle=60.16, dEdgeAngle=60.16, bIsVibro=True)

# PCH result
PCHResult = Calculation.AcousticAnalysis.TransmissionLoss.PCHResult(strPath=PunchFile)  # [hl]
JPT.Debugger(PCHResult)
