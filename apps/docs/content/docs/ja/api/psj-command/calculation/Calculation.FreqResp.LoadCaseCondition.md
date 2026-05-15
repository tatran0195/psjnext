---
title: "Calculation.FreqResp.LoadCaseCondition()"
description: "Set the steady-state excitation input for frequency response (Solver)"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > FreqResp > LoadCase"
macro _link: "[DYNAMIC _FREQ _ANALYSIS _LOADCASE](../../macro/calculation/DYNAMIC _FREQ _ANALYSIS _LOADCASE)"
---

## Description

Set the steady-state excitation input for frequency response (Solver).

## Syntax

```psj
Calculation.FreqResp.LoadCase(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### crTargetAnalysis

- Specify the target analysis to be create a load case. A new analysis is created if this parameter is set as None.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### strName

- Specify the name of load case to be created.
- The default value is "LoadCase1".

<!-- @since:5.1.0 @optional -->
### dFactor

- Specify the load coefficient for the entire load cases to be created.
- The default value is 1.0.

<!-- @since:5.1.0 @optional -->
### iNewID

- Specify the ID of the load case to be created.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### crlSelectedLoad

- Specify the selected loads will be used in the load case to be created.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### dlTargetFactor

- Specify the coefficient for each selected load in the corresponding order.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### crEdit

- Specify an existing load case condition
  - If this parameter is used, the specified load case condition will be modified.
  - If it is left None, a new load case condition will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created frequency load case.

## Sample Code

```psj {9-10}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\plate _eigen.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
# Create a load condition
Calculation.FreqResp.LoadCondition(strName="FRQLoad _1", iLoadDirection=2, dlForce=[0.0, 0.0, 10.0], 
                                    dAmplitude=10.0, crlTargets=[Node(1516)])

# Create a load case
loadCase = Calculation.FreqResp.LoadCaseCondition(crTargetAnalysis=PostFreqAnalysis(1), strName="LoadCase _1", 
                                            crlSelectedLoad=[PostFreqLoad(1)], dlTargetFactor=[1.0])
JPT.Debugger(loadCase)
```
