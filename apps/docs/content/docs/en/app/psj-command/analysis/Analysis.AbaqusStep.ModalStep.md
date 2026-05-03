---
title: "Analysis.AbaqusStep.ModalStep()"
description: "Create Abaqus Step - Modal Type"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Analysis > AbaqusStep > ModalStep"
---

## Description

Create Abaqus Step - Modal Type.

## Syntax

```psj
Analysis.AbaqusStep.ModalStep(...)
```

## Inputs

### `strName` @type(String) @required

- The Modal step name.

### `strDesp` @type(String) @default("")

- The step description of Modal analysis.

### `iEigenSolver` @type(Integer) @default(0)

- The Modal analysis method.
  - 0: Lanczos
  - 1: Subspace

### `iNFreqRequestbchecked` @type(Integer) @default(0)

- The number of modes to obtain.
  - 0: Obtain all modes in the frequency range.
  - Other: specify the number of modes to obtain.

### `ilNFreqRequestTList` @type(List\[Integer]) @default(\[])

- The frequency range.

### `iFreqShiftbchecked` @type(Integer) @default(0)

- The frequency shift value $(cycles/time)^2$.

### `ilFreqShiftTList` @type(List\[Integer]) @default(\[])

- The the frequency shift range.

### `iFreqRangebchecked` @type(Integer) @default(0)

- The minimum frequency of interest $(cycles/time)$.

### `ilFreqRangeTList` @type(List\[Integer]) @default(\[])

- The minimum frequency of interest value list.

### `iIncldAcoustic` @type(Integer) @default(0)

- The inclusion of acoustic-structural coupling.

### `iBlockSizebchecked` @type(Integer) @default(0)

- Whether or not use block size.

### `ilBlockSizeTList` @type(List\[Integer]) @default(\[])

- The block size value list.

### `iMaxBlkNumofLanczosStepbchecked` @type(Integer) @default(0)

- The maximum number of block Lanczos steps.

### `ilMaxBlkNumofLanczosStepTList` @type(List\[Integer]) @default(\[])

- The maximum number of block Lanczos steps value list.

### `iEnableUseSIM` @type(Integer) @default(0)

- The usage of SIM-Based linear dynamic procedures.

### `iEnableIncludeResMods` @type(Integer) @default(0)

- The inclusion of residual modes.

### `iNEigenRequest` @type(Integer) @default(2147483647)

- The number of modes request.

### `iMaxItersUsed` @type(Integer) @default(30)

- The number of iterations allowed before the kernel matrix is reformed.

### `iVectorsUsed` @type(Integer) @default(2147483647)

- The number of vectors used in the iteration.

### `iMethod` @type(Integer) @default(0)

- The solver method.
  - 0: Direct.
  - 1: Iterative.

### `iMatrixStorage` @type(Integer) @default(0)

- How to store the matrix.
  - 0: Default
  - 1: Unsymmetric
  - 2: Symmetric

### `iNormalizeEigenBy` @type(Integer) @default(1)

- The normalization of eigenvectors.
  - 0: Displacement
  - 1: Mass

### `iEvalPropFreqbchecked` @type(Integer) @default(0)

- The frequency for evaluating frequency dependent properties.

### `ilEvalPropFreqTList` @type(List\[Integer]) @default(\[])

- The frequency for evaluating frequency dependent properties value list.

### `abaqusOutputRequest` @type(ABAQUS\_OUTPUT\_REQUEST) @default(ABAQUS\_OUTPUT\_REQUEST)

- List specifying the list of Abaqus output request.

### `crEdit` @type(Cursor) @default(None)

- An existing Abaqus step.
  - If this parameter is used, the specified step will be modified.
  - If it is lef&#x74;_&#x4E;one_, a new step will be created.

## Return Code

A _Cursor_ specifying the newly created or the modified Abaqus Modal step.

## Sample Code

```psj {1-3}
process = Analysis.AbaqusStep.ModalStep(strName="Step1", ilNFreqRequestTList=[DFLT_INT],
  ilFreqShiftTList=[DFLT_DBL], ilFreqRangeTList=[DFLT_DBL, DFLT_DBL],
  ilBlockSizeTList=[DFLT_DBL], ilMaxBlkNumofLanczosStepTList=[0], ilEvalPropFreqTList=[DFLT_DBL])

print("Result Dynamic Process has ID: " + str(process)) #for checking return value
```
