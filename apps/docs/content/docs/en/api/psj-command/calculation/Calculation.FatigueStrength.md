---
title: "Calculation.FatigueStrength()"
description: "Calculate fatigue strength (safety factor, mean stress, stress amplitude) at any location"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > Calculation > FatigueStrength"
macro _link: ""
---

## Description

Calculate fatigue strength (safety factor, mean stress, stress amplitude) at any location.

## Syntax

```psj
Calculation.FatigueStrength(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target. The target can be Part, Face, or Group.

<!-- @since:5.1.0 @type:List[Cursor Pair] @optional @default:[] -->
### `listPropAndMat`

- The property and fatigue material.

<!-- @since:5.1.0 @type:Integer @optional @default:90 -->
### `iResAngle`

- The resolution angle (degree) for calculating the stress in the direction with the minimum safety factor.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iFatigueCriterion`

- The calculation method to be used in fatigue calculations.
  - 0: Calculate the fatigue criterion based on uniaxial fatigue.
  - 1: Calculate the fatigue criterion based on biaxial fatigue.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iTargetElement`

- Whether to recover stress only for elements on the free faces or for all elements in case a solid element part is selected.
  - 0: Recover stress for elements on free faces only.
  - 1: Recover stress for all elements.

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strNewSubcaseName`

- The new subcase name to be created in the created result window.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iSubcaseID`

- The ID of new created subcase.

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strCycleName`

- The cycle name.

<!-- @since:5.1.0 @type:List[Integer] @optional @default:[] -->
### `ilSelectedSubcases`

- The selected subcases.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iCalculationType`

- The calculation type.
  - 0: Minimum Search (Under Development)
  - 1: Node Average (Under Development)
  - 2: Result Average (Under Development)

<!-- @since:5.1.0 @type:List[Integer] @optional @default:[0,0,0] -->
### `ilInitStressSubcases`

- The selected initial stress subcases.

<!-- @since:5.1.0 @type:List[Integer] @optional @default:[0,0,0] -->
### `ilTempSubcases`

- The selected initial stress subcases.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iShellResultType`

- The shell result type.
  - 0: Both
  - 1: Top
  - 2: Bottom

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iStressRange`

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
op2 _path = ".../FatigueStrength.op2"
csv _path = [".../FatigueMaterial.csv"]
# Import result model
Home.ImportResults.Nastran(
    strPath=op2 _path, 
    bReadLoadAndConstraint=True, 
    bReadConnection=True, 
    bCreateResultsAtMidNode=True)

# Durability > Fatigue Material
Calculation.FatigueMaterial(
  strlFilePaths=csv _path)

# Durability > Fatigue Strength
fatigue _strength = Calculation.FatigueStrength(
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
print(fatigue _strength)
```
