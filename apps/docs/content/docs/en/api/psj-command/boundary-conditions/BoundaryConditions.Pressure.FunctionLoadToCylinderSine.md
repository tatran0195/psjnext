---
title: "BoundaryConditions.Pressure.FunctionLoadToCylinderSine()"
description: "Define a pressure load on the selected face or element surface based on a sine function distribution."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > Pressure > FunctionLoadToCylinderSine"
---

## Description

Define a pressure load on the selected face or element surface based on a sine function distribution.

## Syntax

```psj
BoundaryConditions.Pressure.FunctionLoadToCylinderSine(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"PressureSine1" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dA`

- A.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoordinate`

- The coordinate.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dAngleRange`

- The angle range.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bDistributionAxis`

- The distribution axis.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iPressureDirectionMode`

- The pressure direction mode.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bIsTotalForceAdjustment`

- The is total force adjustment.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dTotalForce`

- The total force.

<!-- @since:5.0.1 @type:Vector @optional @default:[0.0,0.0,0.0] -->
### `vecPressureDirection`

- The pressure direction.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoordinateSystemForDirection`

- The coordinate system for direction.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bIsCornerNodesDistribution`

- The is corner nodes distribution.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strFormulaForA`

- The formula for a.

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
BoundaryConditions.Pressure.FunctionLoadToCylinderSine(strName="PressureSine1", dA=0.0, crCoordinate=None, dAngleRange=0.0, bDistributionAxis=False, iPressureDirectionMode=0, bIsTotalForceAdjustment=False, dTotalForce=0.0, vecPressureDirection=[0.0,0.0,0.0], crCoordinateSystemForDirection=None, bIsCornerNodesDistribution=False, strFormulaForA="", crlTargets=[], crEdit=None)
```
