---
title: "Calculation.TransResp.LoadCondition()"
description: "Set the arbitrary excitation input for transient response"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > TransResp > LoadCondition"
macro _link: "[DYNAMIC _TRANS _ANALYSIS _LOAD](../../macro/calculation/DYNAMIC _TRANS _ANALYSIS _LOAD)"
---

## Description

Set the arbitrary excitation input for transient response.

## Syntax

```psj
Calculation.TransResp.LoadCondition(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### crTargetAnalysis

- Specify the target analysis. A new analysis is created if this parameter is set as None.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### crCoordinate

- Specify the coordinate system.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### strName

- Specify the name of load condition to be created.
- The default value is "TRNLoad1".

<!-- @since:5.1.0 @optional -->
### iLoadType

- Specify the load type.
  - 0: Table(TLOAD1)
  - 1: Cosine(TLOAD2)
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iLoadDirection

- Specify the direction of vibration.
  - 0: X
  - 1: Y
  - 2: Z
  - 3: RX
  - 4: RY
  - 5: RZ
  - 6: Normal
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### dlForce

- Specify the vector of vibration force.
- The default value is \[1,0,0].

<!-- @since:5.1.0 @optional -->
### dAmplitude

- Specify the amplitude of vibration load.
- The default value is 1.0.

<!-- @since:5.1.0 @optional -->
### dDelay

- Specify the value of time delay (seconds).
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dPhase

- Specify the value of phase delay (angle) in load type Cosine(TLOAD2).
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### bFt

- Specify whether to use the time history load as inputted value or table.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### dFt

- Specify the value of the time history load.
- The default value is 1.0.

<!-- @since:5.1.0 @optional -->
### crFtCurve

- Specify the field data of the time history load.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### dT1

- Specify the vibration start time of load type Cosine(TLOAD2).
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dT2

- Specify the vibration end time of load type Cosine(TLOAD2).
- The default value is 1.0.

<!-- @since:5.1.0 @optional -->
### dFrequency

- Specify the value of frequency in load type Cosine(TLOAD2).
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dExponent

- Specify the value of exponential function in load type Cosine (TLOAD2).
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dPower

- Specify the value of growth factor in load type Cosine (TLOAD2).
- The default value is 0.0.

<!-- @since:5.1.0 @required -->
### crlTargets

- Specify the selected nodes which can be assigned the load condition.

<!-- @since:5.1.0 @optional -->
### crEdit

- Specify an existing Load condition
  - If this parameter is used, the specified Load condition will be modified.
  - If it is left None, a new Load condition will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created transient load condition.

## Sample Code

```psj {6-8}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\plate _eigen.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Create a load condition
loadcondition = Calculation.TransResp.LoadCondition(strName="TRNLoad _2", iLoadType=1, iLoadDirection=2, 
                                                    dlForce=[0.0, 0.0, 10.0], dAmplitude=10, dT1=0.1, 
                                                    dT2=0.5, dFrequency=10.0, crlTargets=[Node(1516)])
JPT.Debugger(loadcondition)
```
