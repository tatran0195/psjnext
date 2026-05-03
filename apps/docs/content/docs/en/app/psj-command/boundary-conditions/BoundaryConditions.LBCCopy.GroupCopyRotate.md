---
title: "BoundaryConditions.LBCCopy.GroupCopyRotate()"
description: "Copy a group rotate"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > LBCCopy > GroupCopyRotate"
---

## Description

Copy a group rotate.

## Syntax

```psj
BoundaryConditions.LBCCopy.GroupCopyRotate(...)
```

## Inputs

### `iMethod` @type(Integer) @default(1)

- The method.

### `iMatchMethod` @type(Integer) @default(0)

- The match method.

### `posAxis` @type(Position) @default(\[0,0,0])

- The axis.

### `posCenter` @type(Position) @default(\[0,0,0])

- The center.

### `dAngle` @type(Double) @default(0.0)

- The angle.

### `dTol` @type(Double) @default(1)

- The tolerance.

### `crCoord` @type(Cursor) @default(None)

- The coordinate.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.LBCCopy.GroupCopyRotate(iMethod=1, iMatchMethod=0, posAxis=[0,0,0], posCenter=[0,0,0], dAngle=0.0, dTol=1, crCoord=None, crlTargets=[])
```
