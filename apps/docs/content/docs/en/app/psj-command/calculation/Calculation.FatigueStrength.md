---
title: "Calculation.FatigueStrength()"
description: "Calculate fatigue strength (safety factor, mean stress, stress amplitude) at any location"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > Calculation > FatigueStrength"
macro_link: ""
---

## Description

Calculate fatigue strength (safety factor, mean stress, stress amplitude) at any location.

## Syntax

```psj
Calculation.FatigueStrength(...)
```

## Inputs

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target. The target can be Part, Face, or Group.

### `listPropAndMat` @type(List\[Cursor Pair]) @default(\[])

- The property and fatigue material.

### `iResAngle` @type(Integer) @default(90)

- The resolution angle (degree) for calculating the stress in the direction with the minimum safety factor.

### `iFatigueCriterion` @type(Integer) @default(0)

- Calculation method to be used in fatigue calculations.
  - 0: Calculate the fatigue criterion based on uniaxial fatigue.
  - 1: Calculate the fatigue criterion based on biaxial fatigue.

### `iTargetElement` @type(Integer) @default(0)

- Whether to recover stress only for elements on the free faces or for all elements in case a solid element part is selected.
  - 0: Recover stress for elements on free faces only.
  - 1: Recover stress for all elements.

### `strNewSubcaseName` @type(String) @default("")

- New subcase name to be created in the created result window.

### `iSubcaseID` @type(Integer) @default(0)

- The ID of new created subcase.

### `strCycleName` @type(String) @default("")

- The cycle name.

### `ilSelectedSubcases` @type(List\[Integer]) @default(\[])

- Selected subcases.

### `iCalculationType` @type(Integer) @default(0)

- The calculation type.
  - 0: Minimum Search (Under Development)
  - 1: Node Average (Under Development)
  - 2: Result Average (Under Development)

### `ilInitStressSubcases` @type(List\[Integer]) @default(\[0,0,0])

- Selected initial stress subcases.

### `ilTempSubcases` @type(List\[Integer]) @default(\[0,0,0])

- Selected initial stress subcases.

### `iShellResultType` @type(Integer) @default(0)

- The shell result type.
  - 0: Both
  - 1: Top
  - 2: Bottom

### `iStressRange` @type(Integer) @default(0)

- The stress range type.
  - 0: Rainflow
  - 1: MaxMin

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {16-27}
# Please prepare the input files for Durability > Fatigue Strength calculation
op2_path = ".../FatigueStrength.op2"
csv_path = [".../FatigueMaterial.csv"]
# Import result model
Home.ImportResults.Nastran(
    strPath=op2_path, 
    bReadLoadAndConstraint=True, 
    bReadConnection=True, 
    bCreateResultsAtMidNode=True)

# Durability > Fatigue Material
Calculation.FatigueMaterial(
  strlFilePaths=csv_path)

# Durability > Fatigue Strength
fatigue_strength = Calculation.FatigueStrength(
  crlTargets=[Part(1)], 
  listPropAndMat=[CursorPair(Property3DSolid(1), PostFatigueMaterial(1))], 
  iResAngle=9, 
  strNewSubcaseName="Fatigue Strength", 
  iSubcaseID=9, 
  strCycleName="Case 1", 
  ilSelectedSubcases=[[1, 5, 5], [1, 6, 6], [1, 7, 7], [1, 8, 8]], 
  iCalculationType=1, 
  ilInitStressSubcases=[1, 5, 5], 
  ilTempSubcases=[1, 6, 6], 
  iStressRange=1)
print(fatigue_strength)
```
