---
title: "Calculation.Gururi.LoadCase()"
description: "Create a load case for Gururi analysis"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Calculation > Gururi > LoadCase"
macro_link: "[DYNAMIC_FREQ_ANALYSIS_LOADCASE](../../macro/calculation/DYNAMIC_FREQ_ANALYSIS_LOADCASE)"
---

## Description

Create a load case for Gururi analysis.

## Syntax

```psj
Calculation.Gururi.LoadCase(...)
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

### `dlTargetFactor` @type(List\[Double]) @default(\[])

- The coefficient for each selected load in the corresponding order.

### `crEdit` @type(Cursor) @default(None)

- An existing load case condition
  - If this parameter is used, the specified load case condition will be modified.
  - If it is left None, a new load case condition will be created.

## Return Code

A _Cursor_ specifying the created gururi load case.

## Sample Code

```psj {12-13}
# Please set path to your result sample file
samplePath = "C:/Temp/Sample.op2"

# Prepare result model
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60, dEdgeAngle=60)

# Create a load condition
Calculation.Gururi.LoadCondition(strName="FRQLoad_1", iLoadDirection=2, dlForce=[0.0, 0.0, 10.0], 
                                dAmplitude=10.0, crlTargets=[Node(501)])

# Create a load case
loadCase = Calculation.Gururi.LoadCase(crTargetAnalysis=PostFreqAnalysis(1), strName="LoadCase_1", 
                                        crlSelectedLoad=[PostFreqLoad(1)], dlTargetFactor=[1.0])
JPT.Debugger(loadCase)
```
