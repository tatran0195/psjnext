---
title: "Calculation.Subcase.ShowSafety()"
description: "Create a subcase by calculating the safety factor from the selected subcases based on the tolerance of each part"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > Subcase > ShowSafety"
macro _link: "[PostToolsSubcaseSafetyFactor](../../macro/calculation/PostToolsSubcaseSafetyFactor)"
---

## Description

Create a subcase by calculating the safety factor from the selected subcases based on the tolerance of each part.

## Syntax

```psj
Calculation.Subcase.ShowSafety(...)
```

## Inputs

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iAnalysisType`

- The analysis type.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iResultSet`

- The result set.

<!-- @since:5.1.0 @type:List[Integer] @optional @default:[] -->
### `listSubcaseIDs`

- The IDs of selected subcases.

<!-- @since:5.1.0 @type:List[SAFETY _ITEM] @optional @default:SAFETY _ITEM -->
### `listSafetyItems`

- The safety information of each selected target.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iSafetyType`

- The type of safety calculation.
  - 0: YIELD STRESS
  - 1: BREAK STRESS
  - 2: FATIGUE LIMIT

<!-- @since:5.1.0 @type:String @optional @default:"SafetyYield" -->
### `strResultName`

- The name of subcase to be created.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {6-12}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103 _solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Subcase.RelativeOffset
showSafety = Calculation.Subcase.ShowSafety(
    iAnalysisType=2, 
    listSubcaseIDs=[1, 2, 3, 4, 5], 
    listSafetyItems=[
        SAFETY _ITEM(crPart=Part(1), dThreshold=1), 
        SAFETY _ITEM(crPart=Part(2), dThreshold=1), 
        SAFETY _ITEM(crPart=Part(3), dThreshold=1)])
JPT.Debugger(showSafety)
```
