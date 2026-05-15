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

<!-- @since:5.1.0 @optional -->
### iAnalysisType

- Specify the analysis type.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### iResultSet

- Specify result set.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### listSubcaseIDs

- Specify the IDs of selected subcases.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### listSafetyItems

- Specify the safety information of each selected target.
- The default value is [SAFETY\_ITEM](../../data-type/psj-command/parameter-types/SAFETY _ITEM).

<!-- @since:5.1.0 @optional -->
### iSafetyType

- Specify the type of safety calculation.
  - 0: YIELD STRESS
  - 1: BREAK STRESS
  - 2: FATIGUE LIMIT
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### strResultName

- Specify the name of subcase to be created.
- The default value is "SafetyYield".

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
