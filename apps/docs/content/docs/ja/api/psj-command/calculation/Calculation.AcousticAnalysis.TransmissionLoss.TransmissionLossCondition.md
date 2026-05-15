---
title: "Calculation.AcousticAnalysis.TransmissionLoss.TransmissionLossCondition()"
description: "Calculate AC power and transmittance from the selected nodal groups created by importing the PCH file on input side and output side respectively"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > AcousticAnalysis > TransmissionLoss > TransmissionLossCondition"
macro _link: "[AcousticTLCondition](../../macro/calculation/AcousticTLCondition)"
---

## Description

Calculate AC power and transmittance from the selected nodal groups created by importing the PCH file on input side and output side respectively.

## Syntax

```psj
Calculation.AcousticAnalysis.TransmissionLoss.TransmissionLossCondition(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### crGroupIn

- Specify the nodal group of input data.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### crGroupOut

- Specify the nodal group of output data.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### crEdit

- Specify an existing  transmission loss condition
  - If this parameter is used, the specified  transmission loss condition will be modified.
  - If it is left None, a new  transmission loss condition will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created transmission loss condition.

## Sample Code

```psj {10-11}
# Please set path to your sample Nastran Vibro-Acoustic file and Punch file.
ResultFile="C:/Temp/Sample.op2"
PunchFile="C:/Temp/PunchSample.pch"

# Prepare result model
Home.ImportResults.Nastran(strPath=ResultFile, dFaceAngle=60.16, dEdgeAngle=60.16, bIsVibro=True)

# TransmissionLossCondition
Calculation.AcousticAnalysis.TransmissionLoss.PCHResult(strPath=PunchFile)
condition = Calculation.AcousticAnalysis.TransmissionLoss.TransmissionLossCondition(crGroupIn=Group(1), 
                                                                                    crGroupOut=Group(2))
JPT.Debugger(condition)
```
