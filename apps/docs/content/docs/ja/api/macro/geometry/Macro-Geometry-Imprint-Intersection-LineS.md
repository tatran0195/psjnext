---
title: "Imprint _Intersection _LineS()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create imprint Intersection line

## Syntax

```psj
Imprint _Intersection _LineS(cursor[] taCrFaces, bool bBreakFace)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target faces cursor(\[6:Face ID])

<!-- @since:5.0.1 -->
### 2. Bool

Whether break face or not True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Imprint _Intersection _LineS([6:29, 6:24], 1)
```
