---
title: "Capture _CopyToClipboardTileWindow()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Copy tiled image of Main Window to clipboard.
This function works only if Jupiter is running with foreground mode.

## Syntax

```psj
Capture _CopyToClipboardTileWindow(bool WhiteBG)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Bool

White background bool flag true = 1, false = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Capture _CopyToClipboardTileWindow(0)
```
