---
title: "MeshEdit.Import()"
description: "Move nodes deformation"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > Import"
---

## Description

Move nodes deformation

## Syntax

```psj
MeshEdit.Import(iSolverType=0, strFilePath="", iStep=0, dScale=1.0)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### iSolverType

- Specify the solver type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### strFilePath

- Specify the file path.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### iStep

- Specify the step.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dScale

- Specify the scale.
- The default value is 1.0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.Import(iSolverType=0, strFilePath="", iStep=0, dScale=1.0)
```
