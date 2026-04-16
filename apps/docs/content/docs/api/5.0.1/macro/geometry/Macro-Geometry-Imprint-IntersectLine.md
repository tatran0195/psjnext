---
id: Imprint_IntersectLine
title: Imprint_IntersectLine()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Create imprint Intersection line

## Syntax

```psj
Imprint_IntersectLine(int[] FaceID, bool BreakFace,Cursor[] BodyCursor)
```

## Inputs

### `1. Int[]`

Face ID

### `2. Bool`

Flag true = 1,false=0

### `3. Cursor[]`

Body Cursor([3:*]\*=Body ID)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Imprint_IntersectLine([26, 49], 1, [3:1, 3:2])
```
