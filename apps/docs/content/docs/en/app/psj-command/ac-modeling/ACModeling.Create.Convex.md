---
title: "ACModeling.Create.Convex()"
description: "Create Convex In Boundary"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "ACModeling > Create > Convex"
---

## Description

Create Convex In Boundary

## Syntax

```psj
ACModeling.Create.Convex(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @default(\[])

- The part.

### `dMeshSize` @type(Double) @default(0.005)

- The mesh size.

### `dOffset` @type(Double) @default(0.02)

- The offset.

### `dRadius` @type(Double) @default(0.02)

- The radius.

### `iDAxisGround` @type(Integer) @default(0)

- The axis ground.

### `dScale` @type(Double) @default(0.001)

- The scale.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
ACModeling.Create.Convex(crlParts=[], dMeshSize=0.005, dOffset=0.02, dRadius=0.02, iDAxisGround=0, dScale=0.001)
```
