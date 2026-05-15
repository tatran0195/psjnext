---
title: "Analysis.AbaqusStep.ModalStep()"
description: "Create Abaqus Step - Modal Type"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > AbaqusStep > ModalStep"
---

## Description

Create Abaqus Step - Modal Type.

## Syntax

```psj
Analysis.AbaqusStep.ModalStep(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### strName

- Specify the Modal step name.

<!-- @since:5.0.1 @optional -->
### strDesp

- Specify the step description of Modal analysis.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### iEigenSolver

- Specify the Modal analysis method.
  - 0: Lanczos
  - 1: Subspace
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iNFreqRequestbchecked

- Specify the number of modes to obtain.
  - 0: Obtain all modes in the frequency range.
  - Other: specify the number of modes to obtain.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### ilNFreqRequestTList

- Specify the frequency range.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iFreqShiftbchecked

- Specify the frequency shift value $(cycles/time)^2$.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### ilFreqShiftTList

- Specify the the frequency shift range.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iFreqRangebchecked

- Specify the minimum frequency of interest $(cycles/time)$.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### ilFreqRangeTList

- Specify the minimum frequency of interest value list.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iIncldAcoustic

- Specify the inclusion of acoustic-structural coupling.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iBlockSizebchecked

- Specify whether or not use block size.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### ilBlockSizeTList

- Specify the block size value list.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iMaxBlkNumofLanczosStepbchecked

- Specify the maximum number of block Lanczos steps.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### ilMaxBlkNumofLanczosStepTList

- Specify the maximum number of block Lanczos steps value list.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iEnableUseSIM

- Specify the usage of SIM-Based linear dynamic procedures.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iEnableIncludeResMods

- Specify the inclusion of residual modes.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iNEigenRequest

- Specify the number of modes request.
- The default value is 2147483647.

<!-- @since:5.0.1 @optional -->
### iMaxItersUsed

- Specify the number of iterations allowed before the kernel matrix is reformed.
- The default value is 30.

<!-- @since:5.0.1 @optional -->
### iVectorsUsed

- Specify the number of vectors used in the iteration.
- The default value is 2147483647.

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the solver method.
  - 0: Direct.
  - 1: Iterative.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iMatrixStorage

- Specify how to store the matrix.
  - 0: Default
  - 1: Unsymmetric
  - 2: Symmetric
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iNormalizeEigenBy

- Specify the normalization of eigenvectors.
  - 0: Displacement
  - 1: Mass
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### iEvalPropFreqbchecked

- Specify the frequency for evaluating frequency dependent properties.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### ilEvalPropFreqTList

- Specify the frequency for evaluating frequency dependent properties value list.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### abaqusOutputRequest

- Specify the list of Abaqus output request.
- The default value is _[ABAQUS\_OUTPUT\_REQUEST](./../../data-type/psj-command/parameter-types/ABAQUS _OUTPUT _REQUEST)_.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify an existing Abaqus step.
  - If this parameter is used, the specified step will be modified.
  - If it is left _None_, a new step will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the newly created or the modified Abaqus Modal step.

## Sample Code

```psj {1-3}
process = Analysis.AbaqusStep.ModalStep(strName="Step1", ilNFreqRequestTList=[DFLT _INT],
  ilFreqShiftTList=[DFLT _DBL], ilFreqRangeTList=[DFLT _DBL, DFLT _DBL],
  ilBlockSizeTList=[DFLT _DBL], ilMaxBlkNumofLanczosStepTList=[0], ilEvalPropFreqTList=[DFLT _DBL])

print("Result Dynamic Process has ID: " + str(process)) #for checking return value
```
