---
title: "Analysis.Permas.Job()"
description: "Create a Permas Analysis Job"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > Permas > Job"
---

## Description

Create a Permas Analysis Job.

## Syntax

```psj
Analysis.Permas.Job(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:String @required -->
### `strDescription`

- The description.

<!-- @since:5.0.1 @type:Integer @required -->
### `iType`

- The type.
  0: Structure.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crEdit`

- The cursor of the Analysis Permas Job needs editing.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlTargets`

- The targets.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bElStress`

- Whether el stress.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bElStressMis`

- Whether el stress mis.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bElStrain`

- Whether el strain.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bNodeStess`

- Whether node stress.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bGZip`

- Whether G zip.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bIdeas`

- Whether ideas.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bNLResult`

- Whether enable NL Result option.

<!-- @since:5.0.1 @type:Integer @required -->
### `iNLStepType`

- The NL step type.
  0: ALL.
  1: EQUI.
  2: LIST.

<!-- @since:5.0.1 @type:Double @required -->
### `dEquiStart`

- The equi start.

<!-- @since:5.0.1 @type:Double @required -->
### `dEquiStep`

- The equi step.

<!-- @since:5.0.1 @type:Double @required -->
### `dEquiEnd`

- The equi end.

<!-- @since:5.0.1 @type:String @required -->
### `strNLStepList`

- The NL step list.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bTimeStep`

- Whether enable Time Step option.

<!-- @since:5.0.1 @type:Integer @required -->
### `iTimeStepKind`

- The time step kind.
  0: ABS.

<!-- @since:5.0.1 @type:Double @required -->
### `dTimeStart`

- The time start.

<!-- @since:5.0.1 @type:Double @required -->
### `dTimeStep`

- The time step.

<!-- @since:5.0.1 @type:Double @required -->
### `dTimeEnd`

- The time end.

<!-- @since:5.0.1 @type:Integer @required -->
### `iLCId`

- The LC ID.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Analysis.Permas.Job(strName, strDescription, iType, crEdit, crlTargets, bElStress, bElStressMis, bElStrain, bNodeStess, bGZip, bIdeas, bNLResult, iNLStepType, dEquiStart, dEquiStep, dEquiEnd, strNLStepList, bTimeStep, iTimeStepKind, dTimeStart, dTimeStep, dTimeEnd, iLCId)
```
