---
title: "BoundaryConditions.Pressure.Quadratic()"
description: "Create quadratic pressure"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > Pressure > Quadratic"
---

## Description

Create quadratic pressure.

## Syntax

```psj
BoundaryConditions.Pressure.Quadratic(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"PressureQuadratic1" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dA`

- A.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dB`

- The .

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoordinate`

- The coordinate.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dAngleRange`

- The angle range.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iPressureDirectionMode`

- The pressure direction mode.

<!-- @since:5.0.1 @type:Double List @optional @default:[0.0,0.0,0.0] -->
### `dlPressureDirection`

- The pressure direction.

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
BoundaryConditions.Pressure.Quadratic(strName="PressureQuadratic1", dA=0.0, dB=0.0, crCoordinate=None, dAngleRange=0.0, iPressureDirectionMode=0, dlPressureDirection=[0.0,0.0,0.0], crlTargets=[], crEdit=None)
```
