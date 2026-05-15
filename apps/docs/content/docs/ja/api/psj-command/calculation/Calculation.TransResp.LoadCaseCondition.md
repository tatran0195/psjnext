---
title: "Calculation.TransResp.LoadCaseCondition()"
description: "Create a load case for transient response analysis"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > TransResp > LoadCaseCondition"
macro _link: "[DYNAMIC _TRANS _ANALYSIS _LOADCASE](../../macro/calculation/DYNAMIC _TRANS _ANALYSIS _LOADCASE)"
---

## Description

Create a load case for transient response analysis.

## Syntax

```psj
Calculation.TransResp.LoadCaseCondition(...)
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

A _Cursor_ specifying the create transient load case condition.

## Sample Code

```psj {11-12}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\plate _eigen.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Create a load condition
loadcondition = Calculation.TransResp.LoadCondition(strName="TRNLoad _2", iLoadType=1, iLoadDirection=2, 
                                                    dlForce=[0.0, 0.0, 10.0], dAmplitude=10, dT1=0.1, 
                                                    dT2=0.5, dFrequency=10.0, crlTargets=[Node(1516)])

# Create a loadcase
loadcase = Calculation.TransResp.LoadCaseCondition(crTargetAnalysis=PostTransAnalysis(1), strName="LoadCase _1",
                                                 crlSelectedLoad=[PostTransLoad(1)], dlTargetFactor=[1.0])
JPT.Debugger(loadcase)
```
