---
title: "JPT.GetAllAvailableResultOptions()"
description: "Get all available result options of the inputted result type"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get all available result options of the inputted result type.

## Syntax

```psj
JPT.GetAllAvailableResultOptions(PostAnalysisType,
                                 resultSet,
                                 timeStep,
                                 resultName,
                                 componentName,
                                 PostResultDataLoc)
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

## Return Code

A _List of [PostDataOp](../data-type/psj-utility/post-utility/post-built-in-types/post-data-op)_ objects specifying all available settings of the working result.

## Sample Code

```psj {5-13}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101 _solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

all _available _result _options _vector = \
    JPT.GetAllAvailableResultOptions(JPT.PostAnalysisType.POST _ANALYSIS _LINEAR _STATIC,
                                     1,
                                     1,
                                     "Stress",
                                     "XX",
                                     JPT.PostResultDataLoc.POST _LOC _ON _ELEMENT _NODE
                                    )

JPT.Debugger(all _available _result _options _vector)

for available _PostDataOp in all _available _result _options _vector:
    #Component of AvailablePostDataOp
    print("---------------------------------")
    print("Location: " + str(available _PostDataOp.loc))
    print("Conversion: " + str(available _PostDataOp.cnv))
    print("Continuously: " + str(available _PostDataOp.cont))
    print("Coordinate: " + str(available _PostDataOp.coord))
    print("Load 1D: " + str(available _PostDataOp.load1d))
    print("Load 2D: " + str(available _PostDataOp.load2d))
    print("Complex: " + str(available _PostDataOp.complex))
    print("Phase Angle: " + str(available _PostDataOp.phaseAngle))
    print("User Coordinate ID: " + str(available _PostDataOp.userCoordSysId))
```

<!-- [//]: # "amt is not used in the current version"

<!-- print("Amplitude: " + str(available _PostDataOp.amt)) -->
