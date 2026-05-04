---
title: 'Analysis.Permas.Job()'
description: 'Create a Permas Analysis Job'
version_introduced: '5.0.1'
available_versions: 'all'
ribbon: 'Analysis > Permas > Job'
---

## Description

Create a Permas Analysis Job.

## Syntax

```psj
Analysis.Permas.Job(...)
```

## Inputs

### `strName` @type(String) @required

- The name.

### `strDescription` @type(String) @required

- The description.

### `iType` @type(Integer) @required

- The type.
  0: Structure.

### `crEdit` @type(Cursor) @required

- The cursor of the Analysis Permas Job needs editing.

### `crlTargets` @type(List\[Cursor]) @required

- The targets.

### `bElStress` @type(Boolean) @required

- Whether el stress.

### `bElStressMis` @type(Boolean) @required

- Whether el stress mis.

### `bElStrain` @type(Boolean) @required

- Whether el strain.

### `bNodeStess` @type(Boolean) @required

- Whether node stress.

### `bGZip` @type(Boolean) @required

- Whether G zip.

### `bIdeas` @type(Boolean) @required

- Whether ideas.

### `bNLResult` @type(Boolean) @required

- Whether enable NL Result option.

### `iNLStepType` @type(Integer) @required

- The NL step type.
  0: ALL.
  1: EQUI.
  2: LIST.

### `dEquiStart` @type(Double) @required

- The equi start.

### `dEquiStep` @type(Double) @required

- The equi step.

### `dEquiEnd` @type(Double) @required

- The equi end.

### `strNLStepList` @type(String) @required

- The NL step list.

### `bTimeStep` @type(Boolean) @required

- Whether enable Time Step option.

### `iTimeStepKind` @type(Integer) @required

- The time step kind.
  0: ABS.

### `dTimeStart` @type(Double) @required

- The time start.

### `dTimeStep` @type(Double) @required

- The time step.

### `dTimeEnd` @type(Double) @required

- The time end.

### `iLCId` @type(Integer) @required

- The LC ID.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Analysis.Permas.Job(strName, strDescription, iType, crEdit, crlTargets, bElStress, bElStressMis, bElStrain, bNodeStess, bGZip, bIdeas, bNLResult, iNLStepType, dEquiStart, dEquiStep, dEquiEnd, strNLStepList, bTimeStep, iTimeStepKind, dTimeStart, dTimeStep, dTimeEnd, iLCId)
```
