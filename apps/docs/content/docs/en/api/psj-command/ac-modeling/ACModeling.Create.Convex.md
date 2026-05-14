---
title: "ACModeling.Create.Convex()"
description: "Create Convex In Boundary"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "ACModeling > Create > Convex"
---

## Description

Create Convex In Boundary

## Syntax

```psj
ACModeling.Create.Convex(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlParts`

- The part.

<!-- @since:5.0.1 @type:Double @optional @default:0.005 -->
### `dMeshSize`

- The mesh size.

<!-- @since:5.0.1 @type:Double @optional @default:0.02 -->
### `dOffset`

- The offset.

<!-- @since:5.0.1 @type:Double @optional @default:0.02 -->
### `dRadius`

- The radius.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iDAxisGround`

- The axis ground.

<!-- @since:5.0.1 @type:Double @optional @default:0.001 -->
### `dScale`

- The scale.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
ACModeling.Create.Convex(crlParts=[], dMeshSize=0.005, dOffset=0.02, dRadius=0.02, iDAxisGround=0, dScale=0.001)
```
