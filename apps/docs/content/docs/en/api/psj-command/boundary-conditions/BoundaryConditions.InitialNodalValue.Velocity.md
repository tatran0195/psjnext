---
title: "BoundaryConditions.InitialNodalValue.Velocity()"
description: "Create initial velocity"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > InitialNodalValue > Velocity"
---

## Description

Create initial velocity.

## Syntax

```psj
BoundaryConditions.InitialNodalValue.Velocity(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"InitialRotationAngle1" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:ST _DATA @optional @default:LBC _DYNAMIC _INITIAL _CONDITION _DATA() -->
### `stData`

- The data.

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
BoundaryConditions.InitialNodalValue.Velocity(strName="InitialRotationAngle1", stData=LBC _DYNAMIC _INITIAL _CONDITION _DATA(), crlTargets=[], crEdit=None)
```
