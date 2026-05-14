---
title: "Calculation.StressRecovery()"
description: "Recover stresses (strain) in arbitrary elements from the calculation results of RecurDyn"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > Calculation > StressRecovery"
macro _link: ""
---

## Description

Recover stress (strain) in arbitrary elements from the calculation results of RecurDyn.

## Syntax

```psj
Calculation.StressRecovery(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlTargets`

- The target. The target can be Part, Face or Group

<!-- @since:5.1.0 @type:String @optional @default:'' -->
### `strMDFFilePath`

- The MDF file path.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iNodalDisplacement`

- The nodal displacement recovery.
  - 0: No nodal displacement recovery.
  - 1: All nodal displacements recovery.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iElementStress`

- The element stress recovery.
  - 0: No element stress recovery.
  - 1: Specify the element stress for the selected area.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iElementStrain`

- The element strain recovery.
  - 0: No element strain recovery.
  - 1: Specify element strain fort the selected area.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iTargetElement`

- Whether to recover stress only for elements on the free faces or for all elements in case a solid element part is selected.
  - 0: Recover stress for elements on free faces only.
  - 1: Recover stress for all elements.

<!-- @since:5.1.0 @type:List[Double] @optional @default:[] -->
### `dlStep`

- The start-end time step.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bRunSunShine`

- Whether to run the stress recovery calculation by SunShine-Solver.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bImportOP2`

- Whether to read additional Op2 of the stress recovery results.

<!-- @since:5.1.0 @type:String @optional @default:[JPT.GetProgramPath()+"SunShine/tss.bat"] -->
### `strSunShinePath`

- The path of SunShine-Solver.

:::note
When creating a FEM reduced model using the mode synthesis method, be sure to use the same version of SunShine as the one used for stress recovery. If the versions do not match, an error may occur during stress recovery. Even if stress results are obtained, they may not be correct.
:::

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {13-17}
# Please prepare the result files with a compatible version of Sunshine.
op2 _path = ".../StressRecovery.op2"
mdf _path = ".../StressRecovery.mdf"
sunshine _path = ".../tss.bat"
# Import result model
Home.ImportResults.Nastran(
  strPath=op2 _path, 
  bReadLoadAndConstraint=True, 
  bReadConnection=True, 
  bCreateResultsAtMidNode=True)

# Durability > Stress Recovery
stress _recovery = Calculation.StressRecovery(
  crlTargets=[Part(3, 2)], 
  strMDFFilePath=mdf _path, 
  dlStep=[(0.138889, 2.36111), (7.91667, 10.1389)], 
  strSunShinePath=sunshine _path)
print(stress _recovery)
```
