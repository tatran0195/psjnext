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

<!-- @since:5.0.1 @optional -->
### crPart

- Specify the part.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### iType

- Specify the type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bMerge

- Specify the merge.
- The default value is True.

<!-- @since:5.0.1 @optional -->
### posOrgCenter

- Specify the original center.
- The default value is \[0,0,0].

<!-- @since:5.0.1 @optional -->
### vecOrgDirection

- Specify the original direction.
- The default value is \[0,0,0].

<!-- @since:5.0.1 @optional -->
### crCoord

- Specify the coordinate.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### iAxis

- Specify the axis.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dAngle

- Specify the angle.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### bHollow

- Specify the hollow.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### dInnerRadius

- Specify the inner radius.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dOrgOuterRadius

- Specify the original outer radius.
- The default value is 1.0.

<!-- @since:5.0.1 @optional -->
### dTaperAngle

- Specify the taper angle.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iNodeOnCircle

- Specify the node on circle.
- The default value is 12.

<!-- @since:5.0.1 @optional -->
### iNodeOnAxis

- Specify the node on axis.
- The default value is 2.

<!-- @since:5.0.1 @optional -->
### dOriginalHeight

- Specify the original height.
- The default value is 5.0.

## Return Code

_True_ if success, or _False_ if fail.

## Sample Code

```psj
Geometry.Part.Cube()
result = Assemble.AddBoss(crPart=Part(1), iType=1, posOrgCenter=[0, 0.00555556, 0.00555556], vecOrgDirection=[-1.0, 0.0, 0.0], dOrgOuterRadius=1.2)
print(result)
```
