---
title: "JPT.GetAvailableResultOption()"
description: "Get available result option of the inputted result type"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get available result option of the inputted result type.

## Syntax

```psj
JPT.GetAvailableResultOption(PostAnalysisType,
                             resultSet,
                             timeStep,
                             resultName,
                             componentName,
                             PostResultDataLoc,
                             defaultResultOption)
```

## Inputs

<!-- @since:5.0.1 @type:PostAnalysisType @required -->
### `PostAnalysisType`

- The _[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_ describing the type of analysis result.

<!-- @since:5.0.1 @type:Integer @required -->
### `resultSet`

- The step ID of the imported result.

<!-- @since:5.0.1 @type:Integer @required -->
### `timeStep`

- The time step of the imported result.

<!-- @since:5.0.1 @type:String @required -->
### `resultName`

- The type of result (Such as Displacement, Stress, etc.).

<!-- @since:5.0.1 @type:String @required -->
### `componentName`

- A specific direction of the result (Such as X, Y, Z, etc.).

<!-- @since:5.0.1 @type:PostResultDataLoc @required -->
### `PostResultDataLoc`

- The _[PostResultDataLoc](../data-type/psj-utility/post-utility/enumeration-types/post-result-data-loc-types)_ describing the location of result (Such as on node, on element, etc.).

<!-- @since:5.0.1 @type:PostDataOp @required -->
### `defaultResultOption`

- The object specifying the default setting of the working result.

## Return Code

A _[PostDataOp](../data-type/psj-utility/post-utility/post-built-in-types/post-data-op)_ object containing the available setting of the working result.

## Sample Code

```psj {5-20}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101 _solid.op2"
Home.ImportResults.Nastran(strPath=samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

available _result _option = \
    JPT.GetAvailableResultOption(JPT.PostAnalysisType.POST _ANALYSIS _LINEAR _STATIC,
                                 1,
                                 1,
                                 "Displacement",
                                 "X",
                                 JPT.PostResultDataLoc.POST _LOC _ON _NODE,
                                 JPT.GetDefaultResultOption(JPT.PostAnalysisType.POST _ANALYSIS _LINEAR _STATIC,
                                                            1,
                                                            1,
                                                            "Displacement",
                                                            "X",
                                                            JPT.PostResultDataLoc.POST _LOC _ON _NODE)
                                )

JPT.Debugger(available _result _option)

# Component of PostDataOp
print("Location: " + str(available _result _option.loc))
print("Conversion: " + str(available _result _option.cnv))
print("Continuously: " + str(available _result _option.cont))
print("Coordinate: " + str(available _result _option.coord))
print("Load 1D: " + str(available _result _option.load1d))
print("Load 2D: " + str(available _result _option.load2d))
print("Complex: " + str(available _result _option.complex))
print("Phase Angle: " + str(available _result _option.phaseAngle))
print("User Coordinate ID: " + str(available _result _option.userCoordSysId))
```

<!-- [//]: # "amt is not used in the current version"

[//]: # (print("Amplitude: " + str(available _result _option.amt)) -->
