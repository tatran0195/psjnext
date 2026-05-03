---
title: "Calculation.StressRecovery()"
description: "Recover stresses (strain) in arbitrary elements from the calculation results of RecurDyn"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > Calculation > StressRecovery"
macro_link: ""
---

## Description

Recover stress (strain) in arbitrary elements from the calculation results of RecurDyn.

## Syntax

```psj
Calculation.StressRecovery(...)
```

## Inputs

### `crlTargets` @type(List\[Cursor]) @required

- The target. The target can be Part, Face or Group

### `strMDFFilePath` @type(String) @default('')

- The MDF file path.

### `iNodalDisplacement` @type(Integer) @default(1)

- Nodal displacement recovery.
  - 0: No nodal displacement recovery.
  - 1: All nodal displacements recovery.

### `iElementStress` @type(Integer) @default(1)

- Element stress recovery.
  - 0: No element stress recovery.
  - 1: Specify the element stress for the selected area.

### `iElementStrain` @type(Integer) @default(0)

- Element strain recovery.
  - 0: No element strain recovery.
  - 1: Specify element strain fort the selected area.

### `iTargetElement` @type(Integer) @default(0)

- Whether to recover stress only for elements on the free faces or for all elements in case a solid element part is selected.
  - 0: Recover stress for elements on free faces only.
  - 1: Recover stress for all elements.

### `dlStep` @type(List\[Double]) @default(\[])

- The start-end time step.

### `bRunSunShine` @type(Boolean) @default(True)

- Whether to run the stress recovery calculation by SunShine-Solver.

### `bImportOP2` @type(Boolean) @default(True)

- Whether to read additional Op2 of the stress recovery results.

### `strSunShinePath` @type(String) @default(\[JPT.GetProgramPath()+"SunShine/tss.bat"])

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
op2_path = ".../StressRecovery.op2"
mdf_path = ".../StressRecovery.mdf"
sunshine_path = ".../tss.bat"
# Import result model
Home.ImportResults.Nastran(
  strPath=op2_path, 
  bReadLoadAndConstraint=True, 
  bReadConnection=True, 
  bCreateResultsAtMidNode=True)

# Durability > Stress Recovery
stress_recovery = Calculation.StressRecovery(
  crlTargets=[Part(3, 2)], 
  strMDFFilePath=mdf_path, 
  dlStep=[(0.138889, 2.36111), (7.91667, 10.1389)], 
  strSunShinePath=sunshine_path)
print(stress_recovery)
```
