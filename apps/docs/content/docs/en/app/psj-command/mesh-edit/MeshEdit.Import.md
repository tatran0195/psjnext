---
title: "MeshEdit.Import()"
description: "Move nodes deformation"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > Import"
---

## Description

Move nodes deformation

## Syntax

```psj
MeshEdit.Import(iSolverType=0, strFilePath="", iStep=0, dScale=1.0)
```

## Inputs

### `iSolverType` @type(Integer) @default(0)

- The solver type.

### `strFilePath` @type(String) @default("")

- The file path.

### `iStep` @type(Integer) @default(0)

- The step.

### `dScale` @type(Double) @default(1.0)

- The scale.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.Import(iSolverType=0, strFilePath="", iStep=0, dScale=1.0)
```
