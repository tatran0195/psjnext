---
title: "Calculation.Gururi.Response()"
description: "Output the Gururi result of the response point"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Calculation > Gururi > Response"
macro_link: "[DYNAMIC_GURURI_ANALYSIS_RESPONSE](../../macro/calculation/DYNAMIC_GURURI_ANALYSIS_RESPONSE)"
---

## Description

Output the Gururi result of the response point.

## Syntax

```psj
Calculation.Gururi.Response(...)
```

## Inputs

### `crTargetAnalysis` @type(Cursor) @default(None)

- The target job to be processed.

### `crCoordinate` @type(Cursor) @default(None)

- The output coordinate system.

### `bAllModesUsed` @type(Boolean) @default(True)

- Whether to use all modes.

### `strlModesSelected` @type(List\[String]) @default(\[])

- The selected modes using for response calculation. This option was used if bAllModesUsed i&#x73;_&#x46;alse_.

### `bDampingFactor` @type(Boolean) @default(True)

- Whether to use damping factor for calculation.

### `dDampingFactor` @type(Double) @default(1.0)

- The value of damping factor.

### `crDampingFactor` @type(Cursor) @default(None)

- The field data of damping factor.

### `dInputFrequency` @type(Double) @default(0.0)

- The frequency value for analysis.

### `dStartPhrase` @type(Double) @default(0.0)

- The starting phase to analyze.

### `iStepNumber` @type(Integer) @default(10)

- The number division of one cycle.

### `bOutputMaximumGururiResult` @type(Boolean) @default(True)

- Whether to output the maximum result of the selected Principal type and store it in a separated tree of assembly window.

### `iPrincipalType` @type(Integer) @default(3)

- The principal result type that will be analyzed.

### `bAllLoadCases` @type(Boolean) @default(True)

- Whether to use all current load cases.

### `crSelectedLoadCase` @type(Cursor) @default(None)

- The selected load case to analyze. This option was used if bAllLoadCases i&#x73;_&#x46;alse_.

### `crEdit` @type(Cursor) @default(None)

- An existing response condition
  - If this parameter is used, the specified response condition will be modified.
  - If it is left None, a new response condition will be created.

## Return Code

A _Cursor_ specifying the created gururi response condition.

## Sample Code

```psj {16-17}
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

# Response calculation
response = Calculation.Gururi.Response(crTargetAnalysis=PostFreqAnalysis(1), dInputFrequency=180.0, 
                                        iStepNumber=30)
JPT.Debugger(response)
```
