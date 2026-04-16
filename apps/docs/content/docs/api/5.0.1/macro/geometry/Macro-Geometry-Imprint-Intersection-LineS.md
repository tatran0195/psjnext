---
id: Imprint_Intersection_LineS
title: Imprint_Intersection_LineS()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Create imprint Intersection line

## Syntax

```psj
Imprint_Intersection_LineS(cursor[] taCrFaces, bool bBreakFace)
```

## Inputs

### `1. Cursor[]`

Target faces cursor([6:Face ID])

### `2. Bool`

Whether break face or not True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Imprint_Intersection_LineS([6:29, 6:24], 1)
```
