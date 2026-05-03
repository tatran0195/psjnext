---
title: "SNOnePush.AutoSweepClosedLoopShaped()"
description: "Make hexa for closed loop shaped"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "SNOnePush > AutoSweepClosedLoopShaped"
---

## Description

Make hexa for closed loop shaped

## Syntax

```psj
SNOnePush.AutoSweepClosedLoopShaped(crlParts, dMeshSize, dLengthSize)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @required

- The part.

### `dMeshSize` @type(Double) @required

- The mesh size.

### `dLengthSize` @type(Double) @required

- The length size.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
SNOnePush.AutoSweepClosedLoopShaped(crlParts, dMeshSize, dLengthSize)
```
