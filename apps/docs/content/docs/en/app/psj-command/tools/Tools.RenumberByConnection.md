---
title: "Tools.RenumberByConnection()"
description: "Renumber by selection"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > RenumberByConnection"
---

## Description

Renumber by selection

## Syntax

```psj
Tools.RenumberByConnection(connectRenumberTool=CONNECT_RENUMBER_TOOL(), crlTargets=[])
```

## Inputs

### `connectRenumberTool` @type(CONNECT\_RENUMBER\_TOOL) @default(CONNECT\_RENUMBER\_TOOL())

- The renumber tool.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.RenumberByConnection(connectRenumberTool=CONNECT_RENUMBER_TOOL(), crlTargets=[])
```
