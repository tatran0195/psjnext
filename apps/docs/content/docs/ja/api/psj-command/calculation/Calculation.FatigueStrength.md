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

<!-- @since:5.1.0 @optional -->
### crlTargets

- Specify the target. The target can be Part, Face, or Group.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### listPropAndMat

- Specify the property and fatigue material.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### iResAngle

- Specify the resolution angle (degree) for calculating the stress in the direction with the minimum safety factor.
- The default value is 90.

<!-- @since:5.1.0 @optional -->
### iFatigueCriterion

- Specify calculation method to be used in fatigue calculations.
  - 0: Calculate the fatigue criterion based on uniaxial fatigue.
  - 1: Calculate the fatigue criterion based on biaxial fatigue.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iTargetElement

- Specify whether to recover stress only for elements on the free faces or for all elements in case a solid element part is selected.
  - 0: Recover stress for elements on free faces only.
  - 1: Recover stress for all elements.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### strNewSubcaseName

- Specify new subcase name to be created in the created result window.
- The default value is "".

<!-- @since:5.1.0 @optional -->
### iSubcaseID

- Specify the ID of new created subcase.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### strCycleName

- Specify the cycle name.
- The default value is "".

<!-- @since:5.1.0 @optional -->
### ilSelectedSubcases

- Specify selected subcases.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### iCalculationType

- Specify the calculation type.
  - 0: Minimum Search (Under Development)
  - 1: Node Average (Under Development)
  - 2: Result Average (Under Development)
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### ilInitStressSubcases

- Specify selected initial stress subcases.
- The default value is \[0,0,0].

<!-- @since:5.1.0 @optional -->
### ilTempSubcases

- Specify selected initial stress subcases.
- The default value is \[0,0,0].

<!-- @since:5.1.0 @optional -->
### iShellResultType

- Specify the shell result type.
  - 0: Both
  - 1: Top
  - 2: Bottom
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iStressRange

- Specify the stress range type.
  - 0: Rainflow
  - 1: MaxMin
- The default value is 0.

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
