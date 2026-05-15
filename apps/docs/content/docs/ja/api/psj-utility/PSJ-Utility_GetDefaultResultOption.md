---
title: "JPT.GetDefaultResultOption()"
description: "Get default result option setting of the inputted result type"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get default result option setting of the inputted result type.

## Syntax

```psj
JPT.GetDefaultResultOption(PostAnalysisType,
                           resultSet,
                           timeStep,
                           resultName,
                           componentName,
                           PostResultDataLoc)
```

## Inputs

<!-- @since:5.0.1 @required -->
### PostAnalysisType

- Specify the_[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_ describing the type of analysis result.

<!-- @since:5.0.1 @required -->
### resultSet

- Specify the step ID of the imported result.

<!-- @since:5.0.1 @required -->
### timeStep

- Specify the time step of the imported result.

<!-- @since:5.0.1 @required -->
### resultName

- Specify the type of result (Such as Displacement, Stress, etc.).

<!-- @since:5.0.1 @required -->
### componentName

- Specify a specific direction of the result (Such as X, Y, Z, etc.).

<!-- @since:5.0.1 @required -->
### PostResultDataLoc

- Specify the_[PostResultDataLoc](../data-type/psj-utility/post-utility/enumeration-types/post-result-data-loc-types)_ describing the location of result (Such as on node, on element, etc.).

## Return Code

A _[PostDataOp](../data-type/psj-utility/post-utility/post-built-in-types/post-data-op)_ object containing the default setting of the working result.

## Sample Code

```psj {5-12}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101 _solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

default _result _option = \
    JPT.GetDefaultResultOption(JPT.PostAnalysisType.POST _ANALYSIS _LINEAR _STATIC,
                               1,
                               1,
                               "Displacement",
                               "X",
                               1)

JPT.Debugger(default _result _option)

# Component of PostDataOp
print("Location: " + str(default _result _option.loc))
print("Conversion: " + str(default _result _option.cnv))
print("Continuously: " + str(default _result _option.cont))
print("Coordinate: " + str(default _result _option.coord))
print("Load 1D: " + str(default _result _option.load1d))
print("Load 2D: " + str(default _result _option.load2d))
print("Complex: " + str(default _result _option.complex))
print("Phase Angle: " + str(default _result _option.phaseAngle))
print("User Coordinate ID: " + str(default _result _option.userCoordSysId))
```

<!-- [//]: # "amt is not used in the current version"

<!-- print("Amplitude: " + str(default _result _option.amt)) -->
