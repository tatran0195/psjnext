---
title: "Capture _ToPPT()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Save the display window of Jupiter to an image file in pptx.

## Syntax

```psj
Capture _ToPPT(bool bAutoCapture, int[] listAdjust)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Bool

Specify whether crop image to the displayed entity range.

<!-- @since:5.1.0 -->
### 2. int\[]

Specify the left, top, right and bottom margins from the minimized area.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Capture _ToPPT(0, [0,0,0,0])
```
