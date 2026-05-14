---
title: "SNOnePush.AutoSweepClosedLoopShaped()"
description: "Make hexa for closed loop shaped"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "SNOnePush > AutoSweepClosedLoopShaped"
---

## Description

Make hexa for closed loop shaped

## Syntax

```psj
SNOnePush.AutoSweepClosedLoopShaped(crlParts, dMeshSize, dLengthSize)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlParts`

- The part.

<!-- @since:5.0.1 @type:Double @required -->
### `dMeshSize`

- The mesh size.

<!-- @since:5.0.1 @type:Double @required -->
### `dLengthSize`

- The length size.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
SNOnePush.AutoSweepClosedLoopShaped(crlParts, dMeshSize, dLengthSize)
```
