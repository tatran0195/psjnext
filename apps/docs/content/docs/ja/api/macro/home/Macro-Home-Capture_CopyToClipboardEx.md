---
title: "Capture _CopyToClipboardEx()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Copy image of Main Window to clip board.

## Syntax

```psj
Capture _CopyToClipboardEx(bool WhiteBG, bool TransparentBG, bool FixedSize, int exportWidth, int exportHeight, bool bAutoCapture, int[] listAdjust)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Bool

White background bool flag true = 1, false = 0

<!-- @since:5.1.0 -->
### 2. Bool

Transparent background flag true = 1, false = 0

<!-- @since:5.1.0 -->
### 3. Bool

Fixed Size flag true = 1, false = 0

<!-- @since:5.1.0 -->
### 4. Int

Export Width

<!-- @since:5.1.0 -->
### 5. Int

Export Height

<!-- @since:5.1.0 -->
### 6. Bool

Specify whether crop image to the displayed entity range.

<!-- @since:5.1.0 -->
### 7. int\[]

Specify the left, top, right and bottom margins from the minimized area.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Capture _CopyToClipboardEx(0, 0, 0, 1200, 900, 0, [0, 0, 0, 0])
```
