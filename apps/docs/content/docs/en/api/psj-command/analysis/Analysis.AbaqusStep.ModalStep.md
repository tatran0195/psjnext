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

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The Modal step name.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strDesp`

- The step description of Modal analysis.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEigenSolver`

- The Modal analysis method.
  - 0: Lanczos
  - 1: Subspace

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iNFreqRequestbchecked`

- The number of modes to obtain.
  - 0: Obtain all modes in the frequency range.
  - Other: specify the number of modes to obtain.

<!-- @since:5.0.1 @type:List[Integer] @optional @default:[] -->
### `ilNFreqRequestTList`

- The frequency range.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iFreqShiftbchecked`

- The frequency shift value $(cycles/time)^2$.

<!-- @since:5.0.1 @type:List[Integer] @optional @default:[] -->
### `ilFreqShiftTList`

- The frequency shift range.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iFreqRangebchecked`

- The minimum frequency of interest $(cycles/time)$.

<!-- @since:5.0.1 @type:List[Integer] @optional @default:[] -->
### `ilFreqRangeTList`

- The minimum frequency of interest value list.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iIncldAcoustic`

- The inclusion of acoustic-structural coupling.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iBlockSizebchecked`

- Whether or not use block size.

<!-- @since:5.0.1 @type:List[Integer] @optional @default:[] -->
### `ilBlockSizeTList`

- The block size value list.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMaxBlkNumofLanczosStepbchecked`

- The maximum number of block Lanczos steps.

<!-- @since:5.0.1 @type:List[Integer] @optional @default:[] -->
### `ilMaxBlkNumofLanczosStepTList`

- The maximum number of block Lanczos steps value list.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEnableUseSIM`

- The usage of SIM-Based linear dynamic procedures.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEnableIncludeResMods`

- The inclusion of residual modes.

<!-- @since:5.0.1 @type:Integer @optional @default:2147483647 -->
### `iNEigenRequest`

- The number of modes request.

<!-- @since:5.0.1 @type:Integer @optional @default:30 -->
### `iMaxItersUsed`

- The number of iterations allowed before the kernel matrix is reformed.

<!-- @since:5.0.1 @type:Integer @optional @default:2147483647 -->
### `iVectorsUsed`

- The number of vectors used in the iteration.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMethod`

- The solver method.
  - 0: Direct.
  - 1: Iterative.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMatrixStorage`

- The how to store the matrix.
  - 0: Default
  - 1: Unsymmetric
  - 2: Symmetric

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iNormalizeEigenBy`

- The normalization of eigenvectors.
  - 0: Displacement
  - 1: Mass

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEvalPropFreqbchecked`

- The frequency for evaluating frequency dependent properties.

<!-- @since:5.0.1 @type:List[Integer] @optional @default:[] -->
### `ilEvalPropFreqTList`

- The frequency for evaluating frequency dependent properties value list.

<!-- @since:5.0.1 @type:ABAQUS _OUTPUT _REQUEST @optional @default:ABAQUS _OUTPUT _REQUEST -->
### `abaqusOutputRequest`

- The list specifying the list of Abaqus output request.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing Abaqus step.
  - If this parameter is used, the specified step will be modified.
  - If it is left _None_, a new step will be created.

## Return Code

A _Cursor_ specifying the newly created or the modified Abaqus Modal step.

## Sample Code

```psj {1-3}
process = Analysis.AbaqusStep.ModalStep(strName="Step1", ilNFreqRequestTList=[DFLT _INT],
  ilFreqShiftTList=[DFLT _DBL], ilFreqRangeTList=[DFLT _DBL, DFLT _DBL],
  ilBlockSizeTList=[DFLT _DBL], ilMaxBlkNumofLanczosStepTList=[0], ilEvalPropFreqTList=[DFLT _DBL])

print("Result Dynamic Process has ID: " + str(process)) #for checking return value
```
