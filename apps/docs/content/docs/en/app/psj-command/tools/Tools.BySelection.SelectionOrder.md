---
title: "Tools.BySelection.SelectionOrder()"
description: "Renumber by selection order"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > BySelection > SelectionOrder"
---

## Description

Renumber by selection order

## Syntax

```psj
Tools.BySelection.SelectionOrder(crlTargets=[], iType=0, iMethod=0, iStartID=1, iIncrementStep=1, bAscending=True)
```

## Inputs

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `iType` @type(Integer) @default(0)

- The type.

### `iMethod` @type(Integer) @default(0)

- The method.

### `iStartID` @type(Integer) @default(1)

- The start ID.

### `iIncrementStep` @type(Integer) @default(1)

- The increment step.

### `bAscending` @type(Boolean) @default(True)

- The ascending.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.BySelection.SelectionOrder(crlTargets=[], iType=0, iMethod=0, iStartID=1, iIncrementStep=1, bAscending=True)
```
