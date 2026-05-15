---
title: "ImprintOffsetLineS()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create imprint Offset line

## Syntax

```psj
ImprintOffsetLineS(cursor[] face, cursor[] edge, bool bBreakFace, double offsetDistance, int iLayerNumber,
    bool merge, bool extend, int layerMethod, double layerOffset, bool autoCollapse, int RLType)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target face cursor(\[6:Face ID])

<!-- @since:5.0.1 -->
### 2. Cursor\[]

Target edge cursor(\[5:Edge ID])

<!-- @since:5.0.1 -->
### 3. Bool

Whether break face or not True = 1, False = 0

<!-- @since:5.0.1 -->
### 4. Double

Offset distance corresponding to Layer 0

<!-- @since:5.0.1 -->
### 5. Int

Layer number corresponding to Layer 0

<!-- @since:5.0.1 -->
### 6. Bool

Whether merge offset line or not True = 1, False = 0

<!-- @since:5.0.1 -->
### 7. Bool

Whether extend offset line or not True = 1, False = 0

<!-- @since:5.0.1 -->
### 8. Int

Layer method

- 0: Distance with number
- 1: Layer with distance

<!-- @since:5.0.1 -->
### 9. Double

\[Layer offset value] corresponding to Layer 1

<!-- @since:5.0.1 -->
### 10. Bool

Whether auto-collapse or not True = 1, False = 0

<!-- @since:5.0.1 -->
### 11. Int

Option method

- 0: One side, at the original offset direction
- 1: One side, at the opposite side of original offset direction
- 2: Both side

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImprintOffsetLineS([6:67], [5:568], 0, 0.0015, 3, 0, 0, 1, [0.002], 0, 2)
```
