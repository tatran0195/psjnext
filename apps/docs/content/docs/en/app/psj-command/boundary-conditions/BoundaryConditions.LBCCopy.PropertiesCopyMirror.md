---
title: "BoundaryConditions.LBCCopy.PropertiesCopyMirror()"
description: "Copy a property mirror"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > LBCCopy > PropertiesCopyMirror"
---

## Description

Copy a property mirror.

## Syntax

```psj
BoundaryConditions.LBCCopy.PropertiesCopyMirror(...)
```

## Inputs

### `iMethod` @type(Integer) @default(2)

- The method.

### `iMatchMethod` @type(Integer) @default(0)

- The match method.

### `poslPoints` @type(Position List) @default(\[])

- The points.

### `dOffset` @type(Double) @default(0)

- The offset.

### `dTol` @type(Double) @default(1)

- The tolerance.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.LBCCopy.PropertiesCopyMirror(iMethod=2, iMatchMethod=0, poslPoints=[], dOffset=0, dTol=1, crlTargets=[])
```
