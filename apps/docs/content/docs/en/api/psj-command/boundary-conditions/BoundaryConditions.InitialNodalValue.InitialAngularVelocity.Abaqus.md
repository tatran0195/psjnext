---
title: "BoundaryConditions.InitialNodalValue.InitialAngularVelocity.Abaqus()"
description: "Create initial angular velocity for the Abaqus solver"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > InitialNodalValue > InitialAngularVelocity > Abaqus"
---

## Description

Create initial angular velocity for the Abaqus solver.

## Syntax

```psj
BoundaryConditions.InitialNodalValue.InitialAngularVelocity.Abaqus(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"InitialAngularVelocityAbaqus1" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dVelocity`

- The velocity.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strFirstCoord`

- The first coordinate.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strSecondCoord`

- The second coordinate.

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
BoundaryConditions.InitialNodalValue.InitialAngularVelocity.Abaqus(strName="InitialAngularVelocityAbaqus1", dVelocity=DFLT _DBL, strFirstCoord="", strSecondCoord="", crlTargets=[], crEdit=None)
```
