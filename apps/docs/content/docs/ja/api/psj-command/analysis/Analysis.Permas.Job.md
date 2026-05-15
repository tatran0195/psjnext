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

<!-- @since:5.0.1 @required -->
### strName

- Specify the name.

<!-- @since:5.0.1 @required -->
### strDescription

- Specify the description.

<!-- @since:5.0.1 @required -->
### iType

- Specify the type.
  0: Structure.

<!-- @since:5.0.1 @required -->
### crEdit

- Specify the cursor of the Analysis Permas Job needs editing.

<!-- @since:5.0.1 @required -->
### crlTargets

- Specify the targets.

<!-- @since:5.0.1 @required -->
### bElStress

- Specify whether el stress.

<!-- @since:5.0.1 @required -->
### bElStressMis

- Specify whether el stress mis.

<!-- @since:5.0.1 @required -->
### bElStrain

- Specify whether el strain.

<!-- @since:5.0.1 @required -->
### bNodeStess

- Specify whether node stress.

<!-- @since:5.0.1 @required -->
### bGZip

- Specify whether G zip.

<!-- @since:5.0.1 @required -->
### bIdeas

- Specify whether ideas.

<!-- @since:5.0.1 @required -->
### bNLResult

- Specify whether enable NL Result option.

<!-- @since:5.0.1 @required -->
### iNLStepType

- Specify the NL step type.
  0: ALL.
  1: EQUI.
  2: LIST.

<!-- @since:5.0.1 @required -->
### dEquiStart

- Specify the equi start.

<!-- @since:5.0.1 @required -->
### dEquiStep

- Specify the equi step.

<!-- @since:5.0.1 @required -->
### dEquiEnd

- Specify the equi end.

<!-- @since:5.0.1 @required -->
### strNLStepList

- Specify the NL step list.

<!-- @since:5.0.1 @required -->
### bTimeStep

- Specify whether enable Time Step option.

<!-- @since:5.0.1 @required -->
### iTimeStepKind

- Specify the time step kind.
  0: ABS.

<!-- @since:5.0.1 @required -->
### dTimeStart

- Specify the time start.

<!-- @since:5.0.1 @required -->
### dTimeStep

- Specify the time step.

<!-- @since:5.0.1 @required -->
### dTimeEnd

- Specify the time end.

<!-- @since:5.0.1 @required -->
### iLCId

- Specify the LC ID.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Analysis.Permas.Job(strName, strDescription, iType, crEdit, crlTargets, bElStress, bElStressMis, bElStrain, bNodeStess, bGZip, bIdeas, bNLResult, iNLStepType, dEquiStart, dEquiStep, dEquiEnd, strNLStepList, bTimeStep, iTimeStepKind, dTimeStart, dTimeStep, dTimeEnd, iLCId)
```
