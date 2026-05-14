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

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSolverType`

- The solver type.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strFilePath`

- The file path.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iStep`

- The step.

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dScale`

- The scale.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.Import(iSolverType=0, strFilePath="", iStep=0, dScale=1.0)
```
