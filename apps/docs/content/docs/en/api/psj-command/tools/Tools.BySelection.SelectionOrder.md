---
title: "Tools.BySelection.SelectionOrder()"
description: "Renumber by selection order"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > BySelection > SelectionOrder"
---

## Description

Renumber by selection order

## Syntax

```psj
Tools.BySelection.SelectionOrder(crlTargets=[], iType=0, iMethod=0, iStartID=1, iIncrementStep=1, bAscending=True)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iType`

- The type.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMethod`

- The method.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iStartID`

- The start ID.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iIncrementStep`

- The increment step.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bAscending`

- The ascending.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.BySelection.SelectionOrder(crlTargets=[], iType=0, iMethod=0, iStartID=1, iIncrementStep=1, bAscending=True)
```
