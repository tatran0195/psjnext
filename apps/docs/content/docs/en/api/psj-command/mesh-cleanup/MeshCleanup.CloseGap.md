---
title: "MeshCleanup.CloseGap()"
description: "MeshCleanup Cleanup CloseGap"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshCleanup > CloseGap"
---

## Description

MeshCleanup Cleanup CloseGap

## Syntax

```psj
MeshCleanup.CloseGap(crlPartsCur=[], dDistanceTol=0.01)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlPartsCur`

- The part cur.

<!-- @since:5.0.1 @type:Double @optional @default:0.01 -->
### `dDistanceTol`

- The distance tolerance.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.CloseGap(crlPartsCur=[], dDistanceTol=0.01)
```
