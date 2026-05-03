---
title: "MeshCleanup.CloseGap()"
description: "MeshCleanup Cleanup CloseGap"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshCleanup > CloseGap"
---

## Description

MeshCleanup Cleanup CloseGap

## Syntax

```psj
MeshCleanup.CloseGap(crlPartsCur=[], dDistanceTol=0.01)
```

## Inputs

### `crlPartsCur` @type(List\[Cursor]) @default(\[])

- The part cur.

### `dDistanceTol` @type(Double) @default(0.01)

- The distance tolerance.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.CloseGap(crlPartsCur=[], dDistanceTol=0.01)
```
