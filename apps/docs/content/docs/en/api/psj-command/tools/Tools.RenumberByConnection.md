---
title: "Tools.RenumberByConnection()"
description: "Renumber by selection"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > RenumberByConnection"
---

## Description

Renumber by selection

## Syntax

```psj
Tools.RenumberByConnection(connectRenumberTool=CONNECT _RENUMBER _TOOL(), crlTargets=[])
```

## Inputs

<!-- @since:5.0.1 @type:CONNECT _RENUMBER _TOOL @optional @default:CONNECT _RENUMBER _TOOL() -->
### `connectRenumberTool`

- The renumber tool.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.RenumberByConnection(connectRenumberTool=CONNECT _RENUMBER _TOOL(), crlTargets=[])
```
