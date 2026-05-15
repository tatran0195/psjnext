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

<!-- @since:5.0.1 @optional -->
### connectRenumberTool

- Specify the renumber tool.
- The default value is CONNECT\_RENUMBER\_TOOL().

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the target.
- The default value is \[].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.RenumberByConnection(connectRenumberTool=CONNECT _RENUMBER _TOOL(), crlTargets=[])
```
