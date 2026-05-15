---
title: "Imprint _ProjectionLine()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create imprint Projection line

## Syntax

```psj
Imprint _ProjectionLine(int[] EdgeID, int[] FaceID, bool BreakFace,Cursor[] BodyCursor)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. int\[]

Edge ID

<!-- @since:5.0.1 -->
### 2. int\[]

Face ID

<!-- @since:5.0.1 -->
### 3. bool

Flag Break Face true = 1,false=0

<!-- @since:5.0.1 -->
### 4. Cursor\[]

Body Cursor(\[3:\*]\*=Body ID)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Imprint _ProjectionLine([35], [26], 1, [3:1, 3:2])
```
