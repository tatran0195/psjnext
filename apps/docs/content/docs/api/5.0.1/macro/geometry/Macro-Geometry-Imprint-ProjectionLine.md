---
id: Imprint_ProjectionLine
title: Imprint_ProjectionLine()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Create imprint Projection line

## Syntax

```psj
Imprint_ProjectionLine(int[] EdgeID, int[] FaceID, bool BreakFace,Cursor[] BodyCursor)
```

## Inputs

### `1. int[]`

Edge ID

### `2. int[]`

Face ID

### `3. bool`

Flag Break Face true = 1,false=0

### `4. Cursor[]`

Body Cursor([3:*]\*=Body ID)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Imprint_ProjectionLine([35], [26], 1, [3:1, 3:2])
```
