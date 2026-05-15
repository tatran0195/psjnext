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

<!-- @since:5.0.1 @optional -->
### crlPartsCur

- Specify the part cur.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dDistanceTol

- Specify the distance tolerance.
- The default value is 0.01.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.CloseGap(crlPartsCur=[], dDistanceTol=0.01)
```
