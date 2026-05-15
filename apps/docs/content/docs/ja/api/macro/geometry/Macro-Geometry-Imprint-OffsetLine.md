---
title: "Imprint _OffsetLine()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create imprint Offset line

## Syntax

```psj
Imprint _OffsetLine(int[] FaceID, int[] EdgeID, double Offset, bool Flag _Extend, bool BreakFace,Cursor[] BodyCursor)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int\[]

Face ID

<!-- @since:5.0.1 -->
### 2. Int\[]

Edge ID

<!-- @since:5.0.1 -->
### 3. Double

Offset Value

<!-- @since:5.0.1 -->
### 4. Bool

Flag Extend true = 1,false=0

<!-- @since:5.0.1 -->
### 5. Bool

Flag Break true = 1,false=0

<!-- @since:5.0.1 -->
### 6. Cursor\[]

Body Cursor(\[3:\*]\*=Body ID)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Imprint _OffsetLine([26], [18], 0.005, 1, 1, [3:1])
```
