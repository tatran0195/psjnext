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

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crTargetAnalysis`

- The target analysis to be create a load case. A new analysis is created if this parameter is set as None.

<!-- @since:5.1.0 @type:String @optional @default:"LoadCase1" -->
### `strName`

- The name of load case to be created.

<!-- @since:5.1.0 @type:Double @optional @default:1.0 -->
### `dFactor`

- The load coefficient for the entire load cases to be created.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iNewID`

- The ID of the load case to be created.

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlSelectedLoad`

- The selected loads will be used in the load case to be created.

<!-- @since:5.1.0 @type:Double List @optional @default:[] -->
### `dlTargetFactor`

- The coefficient for each selected load in the corresponding order.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing load case condition
  - If this parameter is used, the specified load case condition will be modified.
  - If it is left None, a new load case condition will be created.

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
