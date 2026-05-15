---
title: "Calculation.Gururi.LoadCase()"
description: "Create a load case for Gururi analysis"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > Gururi > LoadCase"
macro _link: "[DYNAMIC _FREQ _ANALYSIS _LOADCASE](../../macro/calculation/DYNAMIC _FREQ _ANALYSIS _LOADCASE)"
---

## Description

Create a load case for Gururi analysis.

## Syntax

```psj
Calculation.Gururi.LoadCase(...)
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

A _Cursor_ specifying the created gururi load case.

## Sample Code

```psj {12-13}
# Please set path to your result sample file
samplePath = "C:/Temp/Sample.op2"

# Prepare result model
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60, dEdgeAngle=60)

# Create a load condition
Calculation.Gururi.LoadCondition(strName="FRQLoad _1", iLoadDirection=2, dlForce=[0.0, 0.0, 10.0], 
                                dAmplitude=10.0, crlTargets=[Node(501)])

# Create a load case
loadCase = Calculation.Gururi.LoadCase(crTargetAnalysis=PostFreqAnalysis(1), strName="LoadCase _1", 
                                        crlSelectedLoad=[PostFreqLoad(1)], dlTargetFactor=[1.0])
JPT.Debugger(loadCase)
```
