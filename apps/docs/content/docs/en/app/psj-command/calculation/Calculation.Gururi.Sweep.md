---
title: "Calculation.Gururi.Sweep()"
description: "Output specified element/frequency result output to external file"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Calculation > Gururi > Sweep"
macro_link: "[DYNAMIC_GURURI_ANALYSIS_SWEEP](../../macro/calculation/DYNAMIC_GURURI_ANALYSIS_SWEEP)"
---

## Description

Output specified element/frequency result output to external file.

## Syntax

```psj
Calculation.Gururi.Sweep(...)
```

## Inputs

### `strExportPath` @type(String) @required

- The path of result file to be exported.

### `crlTargets` @type(List\[Cursor]) @required

- The target solid elements.

### `crTargetAnalysis` @type(Cursor) @default(None)

- The target job to be processed.

### `crCoordinate` @type(Cursor) @default(None)

- The response points coordinate system.

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

### `dlInputFrequency` @type(Double List) @default(\[])

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

- An existing Load condition
  - If this parameter is used, the specified Load condition will be modified.
  - If it is left None, a new Load condition will be created.

## Return Code

A _Cursor_ specifying the created gururi sweep condition.

## Sample Code

```psj {16-18}
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

# Sweep calculation
sweepResponse = Calculation.Gururi.Sweep(strExportPath="C:/temp/SweepResult.csv", crlTargets=[ROElem(1486)], 
                                        crTargetAnalysis=PostFreqAnalysis(1), dlInputFrequency=[1000.0, 2000.0], 
                                        iStepNumber=30)
JPT.Debugger(sweepResponse)
```
