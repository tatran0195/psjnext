---
title: "Calculation.TransResp.LoadCaseCondition()"
description: "Create a load case for transient response analysis"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Calculation > TransResp > LoadCaseCondition"
macro_link: "[DYNAMIC_TRANS_ANALYSIS_LOADCASE](../../macro/calculation/DYNAMIC_TRANS_ANALYSIS_LOADCASE)"
---

## Description

Create a load case for transient response analysis.

## Syntax

```psj
Calculation.TransResp.LoadCaseCondition(...)
```

## Inputs

### `crTargetAnalysis` @type(Cursor) @default(None)

- The target analysis to be create a load case. A new analysis is created if this parameter is set as None.

### `strName` @type(String) @default("LoadCase1")

- The name of load case to be created.

### `dFactor` @type(Double) @default(1.0)

- The load coefficient for the entire load cases to be created.

### `iNewID` @type(Integer) @default(1)

- The ID of the load case to be created.

### `crlSelectedLoad` @type(List\[Cursor]) @default(\[])

- The selected loads will be used in the load case to be created.

### `dlTargetFactor` @type(Double List) @default(\[])

- The coefficient for each selected load in the corresponding order.

### `crEdit` @type(Cursor) @default(None)

- An existing load case condition
  - If this parameter is used, the specified load case condition will be modified.
  - If it is left None, a new load case condition will be created.

## Return Code

A _Cursor_ specifying the create transient load case condition.

## Sample Code

```psj {11-12}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\plate_eigen.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Create a load condition
loadcondition = Calculation.TransResp.LoadCondition(strName="TRNLoad_2", iLoadType=1, iLoadDirection=2, 
                                                    dlForce=[0.0, 0.0, 10.0], dAmplitude=10, dT1=0.1, 
                                                    dT2=0.5, dFrequency=10.0, crlTargets=[Node(1516)])

# Create a loadcase
loadcase = Calculation.TransResp.LoadCaseCondition(crTargetAnalysis=PostTransAnalysis(1), strName="LoadCase_1",
                                                 crlSelectedLoad=[PostTransLoad(1)], dlTargetFactor=[1.0])
JPT.Debugger(loadcase)
```
