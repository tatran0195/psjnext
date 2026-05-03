---
title: "Assemble.AddBoss()"
description: "Add boss shape to specific body as a union part"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Assemble > Add BOSS"
---

## Description

Add boss shape to specific body as a union part.

## Syntax

```psj
Assemble.AddBoss(...)
```

## Inputs

### `crPart` @type(Cursor) @default(None)

- The part.

### `iType` @type(Integer) @default(0)

- The type.

### `bMerge` @type(Boolean) @default(True)

- The merge.

### `posOrgCenter` @type(Position) @default(\[0,0,0])

- The original center.

### `vecOrgDirection` @type(Vector) @default(\[0,0,0])

- The original direction.

### `crCoord` @type(Cursor) @default(None)

- The coordinate.

### `iAxis` @type(Integer) @default(0)

- The axis.

### `dAngle` @type(Double) @default(0.0)

- The angle.

### `bHollow` @type(Boolean) @default(False)

- The hollow.

### `dInnerRadius` @type(Double) @default(0.0)

- The inner radius.

### `dOrgOuterRadius` @type(Double) @default(1.0)

- The original outer radius.

### `dTaperAngle` @type(Double) @default(0.0)

- The taper angle.

### `iNodeOnCircle` @type(Integer) @default(12)

- The node on circle.

### `iNodeOnAxis` @type(Integer) @default(2)

- The node on axis.

### `dOriginalHeight` @type(Double) @default(5.0)

- The original height.

## Return Code

_True_ if success, or _False_ if fail.

## Sample Code

```psj
Geometry.Part.Cube()
result = Assemble.AddBoss(crPart=Part(1), iType=1, posOrgCenter=[0, 0.00555556, 0.00555556], vecOrgDirection=[-1.0, 0.0, 0.0], dOrgOuterRadius=1.2)
print(result)
```
