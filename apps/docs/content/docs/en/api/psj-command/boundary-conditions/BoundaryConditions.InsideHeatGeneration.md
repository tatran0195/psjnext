---
title: "BoundaryConditions.InsideHeatGeneration()"
description: "Create load boundary condition of inside heat generation"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > InsideHeatGeneration"
---

## Description

Create load boundary condition of inside heat generation.

## Syntax

```psj
BoundaryConditions.InsideHeatGeneration(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"InsideHeatGeneration1" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dInsideFlux`

- The inside flux.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crTable`

- The table.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.InsideHeatGeneration(strName="InsideHeatGeneration1", dInsideFlux=DFLT _DBL, crTable=None, crlTargets=[], crEdit=None)
```
