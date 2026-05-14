---
title: "Assemble.AddBoss()"
description: "Add boss shape to specific body as a union part"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Assemble > Add BOSS"
---

## Description

Add boss shape to specific body as a union part.

## Syntax

```psj
Assemble.AddBoss(...)
```

## Inputs

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crPart`

- The part.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iType`

- The type.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bMerge`

- The merge.

<!-- @since:5.0.1 @type:Position @optional @default:[0,0,0] -->
### `posOrgCenter`

- The original center.

<!-- @since:5.0.1 @type:Vector @optional @default:[0,0,0] -->
### `vecOrgDirection`

- The original direction.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoord`

- The coordinate.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAxis`

- The axis.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dAngle`

- The angle.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bHollow`

- The hollow.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dInnerRadius`

- The inner radius.

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dOrgOuterRadius`

- The original outer radius.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dTaperAngle`

- The taper angle.

<!-- @since:5.0.1 @type:Integer @optional @default:12 -->
### `iNodeOnCircle`

- The node on circle.

<!-- @since:5.0.1 @type:Integer @optional @default:2 -->
### `iNodeOnAxis`

- The node on axis.

<!-- @since:5.0.1 @type:Double @optional @default:5.0 -->
### `dOriginalHeight`

- The original height.

## Return Code

_True_ if success, or _False_ if fail.

## Sample Code

```psj
Geometry.Part.Cube()
result = Assemble.AddBoss(crPart=Part(1), iType=1, posOrgCenter=[0, 0.00555556, 0.00555556], vecOrgDirection=[-1.0, 0.0, 0.0], dOrgOuterRadius=1.2)
print(result)
```
