---
title: "Calculation.Subcase.ShowSafety()"
description: "Create a subcase by calculating the safety factor from the selected subcases based on the tolerance of each part"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Calculation > Subcase > ShowSafety"
macro_link: "[PostToolsSubcaseSafetyFactor](../../macro/calculation/PostToolsSubcaseSafetyFactor)"
---

## Description

Create a subcase by calculating the safety factor from the selected subcases based on the tolerance of each part.

## Syntax

```psj
Calculation.Subcase.ShowSafety(...)
```

## Inputs

### `iAnalysisType` @type(Integer) @default(1)

- The analysis type.

### `iResultSet` @type(Integer) @default(1)

- Result set.

### `listSubcaseIDs` @type(List\[Integer]) @default(\[])

- The IDs of selected subcases.

### `listSafetyItems` @type(List\[SAFETY\_ITEM]) @default(SAFETY\_ITEM)

- The safety information of each selected target.

### `iSafetyType` @type(Integer) @default(0)

- The type of safety calculation.
  - 0: YIELD STRESS
  - 1: BREAK STRESS
  - 2: FATIGUE LIMIT

### `strResultName` @type(String) @default("SafetyYield")

- The name of subcase to be created.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {6-12}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Subcase.RelativeOffset
showSafety = Calculation.Subcase.ShowSafety(
    iAnalysisType=2, 
    listSubcaseIDs=[1, 2, 3, 4, 5], 
    listSafetyItems=[
        SAFETY_ITEM(crPart=Part(1), dThreshold=1), 
        SAFETY_ITEM(crPart=Part(2), dThreshold=1), 
        SAFETY_ITEM(crPart=Part(3), dThreshold=1)])
JPT.Debugger(showSafety)
```
