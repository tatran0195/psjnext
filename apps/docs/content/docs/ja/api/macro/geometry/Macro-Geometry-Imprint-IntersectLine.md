---
title: "Imprint _IntersectLine()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create imprint Intersection line

## Syntax

```psj
Imprint _IntersectLine(int[] FaceID, bool BreakFace,Cursor[] BodyCursor)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int\[]

Face ID

<!-- @since:5.0.1 -->
### 2. Bool

Flag true = 1,false=0

<!-- @since:5.0.1 -->
### 3. Cursor\[]

Body Cursor(\[3:\*]\*=Body ID)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Imprint _IntersectLine([26, 49], 1, [3:1, 3:2])
```
