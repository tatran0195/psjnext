# Title:   Calculation.AcousticAnalysis.TransmissionLoss.TransmissionLossCondition()
# Desc:    Calculate AC power and transmittance from the selected nodal groups created by importing the PCH file on input side and output side respectively
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/calculation/Calculation.AcousticAnalysis.TransmissionLoss.TransmissionLossCondition
# ---
# Please set path to your sample Nastran Vibro-Acoustic file and Punch file.
ResultFile="C:/Temp/Sample.op2"
PunchFile="C:/Temp/PunchSample.pch"

# Prepare result model
Home.ImportResults.Nastran(strPath=ResultFile, dFaceAngle=60.16, dEdgeAngle=60.16, bIsVibro=True)

# TransmissionLossCondition
Calculation.AcousticAnalysis.TransmissionLoss.PCHResult(strPath=PunchFile)
condition = Calculation.AcousticAnalysis.TransmissionLoss.TransmissionLossCondition(crGroupIn=Group(1),   # [hl:start]
                                                                                    crGroupOut=Group(2))  # [hl:end]
JPT.Debugger(condition)
