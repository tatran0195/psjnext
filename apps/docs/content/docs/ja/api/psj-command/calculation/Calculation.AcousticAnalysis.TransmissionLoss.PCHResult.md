---
title: "Calculation.AcousticAnalysis.TransmissionLoss.PCHResult()"
description: "Read a Punch file (*.pch) containing information on the coupled surfaces output from a Nastran structural-acoustic coupled calculation and create a nodal group on the acoustic model"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > AcousticAnalysis > TransmissionLoss > PCHResult"
macro _link: "[AcousticTLPCHResult](../../macro/calculation/AcousticTLPCHResult)"
---

## Description

Read a Punch file (\*.pch) containing information on the coupled surfaces output from a Nastran structural-acoustic coupled calculation and create a nodal group on the acoustic model.

## Syntax

```psj
Calculation.AcousticAnalysis.TransmissionLoss.PCHResult(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### strPath

- Specify the path of (\*.pch) file.

## Return Code

A _Cursor_ specifying the created PHC result.

## Sample Code

```psj {9}
# Please set path to your sample Nastran Vibro-Acoustic file and Punch file.
ResultFile="C:/Temp/Sample.op2"
PunchFile="C:/Temp/PunchSample.pch"

# Prepare result model
Home.ImportResults.Nastran(strPath=ResultFile, dFaceAngle=60.16, dEdgeAngle=60.16, bIsVibro=True)

# PCH result
PCHResult = Calculation.AcousticAnalysis.TransmissionLoss.PCHResult(strPath=PunchFile)
JPT.Debugger(PCHResult)
```
