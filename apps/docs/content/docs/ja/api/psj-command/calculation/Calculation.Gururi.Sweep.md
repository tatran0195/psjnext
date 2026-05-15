---
title: "Calculation.Gururi.Sweep()"
description: "Output specified element/frequency result output to external file"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > Gururi > Sweep"
macro _link: "[DYNAMIC _GURURI _ANALYSIS _SWEEP](../../macro/calculation/DYNAMIC _GURURI _ANALYSIS _SWEEP)"
---

## Description

Output specified element/frequency result output to external file.

## Syntax

```psj
Calculation.Gururi.Sweep(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### strExportPath

- Specify the path of result file to be exported.

<!-- @since:5.1.0 @required -->
### crlTargets

- Specify the target solid elements.

<!-- @since:5.1.0 @optional -->
### crTargetAnalysis

- Specify the target job to be processed.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### crCoordinate

- Specify the response points coordinate system.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### bAllModesUsed

- Specify whether to use all modes.
- The default value is _True_.

<!-- @since:5.1.0 @optional -->
### strlModesSelected

- Specify the selected modes using for response calculation. This option was used if bAllModesUsed is _False_.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### bDampingFactor

- Specify whether to use damping factor for calculation.
- The default value is _True_.

<!-- @since:5.1.0 @optional -->
### dDampingFactor

- Specify the value of damping factor.
- The default value is 1.0.

<!-- @since:5.1.0 @optional -->
### crDampingFactor

- Specify the field data of damping factor.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### dlInputFrequency

- Specify the frequency value for analysis.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### dStartPhrase

- Specify the starting phase to analyze.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### iStepNumber

- Specify the number division of one cycle.
- The default value is 10.

<!-- @since:5.1.0 @optional -->
### bOutputMaximumGururiResult

- Specify whether to output the maximum result of the selected Principal type and store it in a separated tree of assembly window.
- The default value is _True_.

<!-- @since:5.1.0 @optional -->
### iPrincipalType

- Specify the principal result type that will be analyzed.
- The default value is 3.

<!-- @since:5.1.0 @optional -->
### bAllLoadCases

- Specify whether to use all current load cases.
- The default value is _True_.

<!-- @since:5.1.0 @optional -->
### crSelectedLoadCase

- Specify the selected load case to analyze. This option was used if bAllLoadCases is _False_.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### crEdit

- Specify an existing Load condition
  - If this parameter is used, the specified Load condition will be modified.
  - If it is left None, a new Load condition will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created gururi sweep condition.

## Sample Code

```psj {16-18}
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

# Sweep calculation
sweepResponse = Calculation.Gururi.Sweep(strExportPath="C:/temp/SweepResult.csv", crlTargets=[ROElem(1486)], 
                                        crTargetAnalysis=PostFreqAnalysis(1), dlInputFrequency=[1000.0, 2000.0], 
                                        iStepNumber=30)
JPT.Debugger(sweepResponse)
```
