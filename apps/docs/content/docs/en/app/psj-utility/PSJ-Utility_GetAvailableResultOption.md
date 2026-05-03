---
title: "JPT.GetAvailableResultOption()"
description: "Get available result option of the inputted result type"
version_introduced: "5.0.1"
available_versions: "all"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

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

### `PostAnalysisType` @type(Enum) @required

- Th&#x65;_[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_&#x64;escribing the type of analysis result.

### `resultSet` @type(Integer) @required

- The step ID of the imported result.

### `timeStep` @type(Integer) @required

- The time step of the imported result.

### `resultName` @type(String) @required

- The type of result (Such as Displacement, Stress, etc.).

### `componentName` @type(String) @required

- A specific direction of the result (Such as X, Y, Z, etc.).

### `PostResultDataLoc` @type(Enum) @required

- Th&#x65;_[PostResultDataLoc](../data-type/psj-utility/post-utility/enumeration-types/post-result-data-loc-types)_&#x64;escribing the location of result (Such as on node, on element, etc.).

### `defaultResultOption` @type(PostDataOp) @required

- Object specifying the default setting of the working result.

## Return Code

A _[PostDataOp](../data-type/psj-utility/post-utility/post-built-in-types/post-data-op)_ object containing the available setting of the working result.

## Sample Code

```psj {5-20}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
Home.ImportResults.Nastran(strPath=samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

available_result_option = \
    JPT.GetAvailableResultOption(JPT.PostAnalysisType.POST_ANALYSIS_LINEAR_STATIC,
                                 1,
                                 1,
                                 "Displacement",
                                 "X",
                                 JPT.PostResultDataLoc.POST_LOC_ON_NODE,
                                 JPT.GetDefaultResultOption(JPT.PostAnalysisType.POST_ANALYSIS_LINEAR_STATIC,
                                                            1,
                                                            1,
                                                            "Displacement",
                                                            "X",
                                                            JPT.PostResultDataLoc.POST_LOC_ON_NODE)
                                )

JPT.Debugger(available_result_option)

# Component of PostDataOp
print("Location: " + str(available_result_option.loc))
print("Conversion: " + str(available_result_option.cnv))
print("Continuously: " + str(available_result_option.cont))
print("Coordinate: " + str(available_result_option.coord))
print("Load 1D: " + str(available_result_option.load1d))
print("Load 2D: " + str(available_result_option.load2d))
print("Complex: " + str(available_result_option.complex))
print("Phase Angle: " + str(available_result_option.phaseAngle))
print("User Coordinate ID: " + str(available_result_option.userCoordSysId))
```

<!-- [//]: # "amt is not used in the current version"

[//]: # (print("Amplitude: " + str(available_result_option.amt)) -->
