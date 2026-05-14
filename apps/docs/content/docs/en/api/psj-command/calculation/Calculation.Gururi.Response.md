---
title: "Calculation.Gururi.Response()"
description: "Output the Gururi result of the response point"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > Gururi > Response"
macro _link: "[DYNAMIC _GURURI _ANALYSIS _RESPONSE](../../macro/calculation/DYNAMIC _GURURI _ANALYSIS _RESPONSE)"
---

## Description

Output the Gururi result of the response point.

## Syntax

```psj
Calculation.Gururi.Response(...)
```

## Inputs

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crTargetAnalysis`

- The target job to be processed.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crCoordinate`

- The output coordinate system.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bAllModesUsed`

- Whether to use all modes.

<!-- @since:5.1.0 @type:List[String] @optional @default:[] -->
### `strlModesSelected`

- The selected modes using for response calculation. This option was used if bAllModesUsed is _False_.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bDampingFactor`

- Whether to use damping factor for calculation.

<!-- @since:5.1.0 @type:Double @optional @default:1.0 -->
### `dDampingFactor`

- The value of damping factor.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crDampingFactor`

- The field data of damping factor.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dInputFrequency`

- The frequency value for analysis.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dStartPhrase`

- The starting phase to analyze.

<!-- @since:5.1.0 @type:Integer @optional @default:10 -->
### `iStepNumber`

- The number division of one cycle.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bOutputMaximumGururiResult`

- Whether to output the maximum result of the selected Principal type and store it in a separated tree of assembly window.

<!-- @since:5.1.0 @type:Integer @optional @default:3 -->
### `iPrincipalType`

- The principal result type that will be analyzed.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bAllLoadCases`

- Whether to use all current load cases.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crSelectedLoadCase`

- The selected load case to analyze. This option was used if bAllLoadCases is _False_.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crEdit`

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
Calculation.Gururi.LoadCondition(strName="FRQLoad _1", iLoadDirection=2, dlForce=[0.0, 0.0, 10.0], 
                                dAmplitude=10.0, crlTargets=[Node(501)])

# Create a load case
loadCase = Calculation.Gururi.LoadCase(crTargetAnalysis=PostFreqAnalysis(1), strName="LoadCase _1", 
                                        crlSelectedLoad=[PostFreqLoad(1)], dlTargetFactor=[1.0])

# Response calculation
response = Calculation.Gururi.Response(crTargetAnalysis=PostFreqAnalysis(1), dInputFrequency=180.0, 
                                        iStepNumber=30)
JPT.Debugger(response)
```
