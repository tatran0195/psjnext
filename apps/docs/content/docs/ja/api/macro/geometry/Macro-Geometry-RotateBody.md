---
title: "RotateBody()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Rotate Body

## Syntax

```psj
RotateBody(cursor[] taBody, double[3] vdCenter, double[3] vdAxis, double angle,
    bool createNewBody, bool copyLBC, int copyCount, bool mergeNode, double dTolerance)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target part cursor(\[3:Part ID])

<!-- @since:5.0.1 -->
### 2. Double\[3]

Rotation coordinate Point(\[x, y, z])

<!-- @since:5.0.1 -->
### 3. Double\[3]

Rotation axis

<!-- @since:5.0.1 -->
### 4. Double

Rotation angle (radian)

<!-- @since:5.0.1 -->
### 5. Bool

Create new part bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 6. Bool

LBC copy bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 7. Int

Copy Count value

<!-- @since:5.0.1 -->
### 8. Bool

Equivalence nodes bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 9. Double

Equivalence tolerance

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
RotateBody([3:1], [0, 0, 0.0055556], [0, 0, 0.001], 0.523599, 1, 0, 1, 0, 1e-08)
```
