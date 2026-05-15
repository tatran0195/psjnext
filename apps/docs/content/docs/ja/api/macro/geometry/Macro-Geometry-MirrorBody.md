---
title: "MirrorBody()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Mirror Body

## Syntax

```psj
MirrorBody(cursor[] taBody, double[] scaleVector, double dOffset, bool bCreateNewBody,
    bool bCopyLBC, bool bCopyProperty, bool bRemoveDupFace, bool bMergeNode, double dTolerance)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target part cursor(\[3:Part ID])

<!-- @since:5.0.1 -->
### 2. Double\[]

Mirror plane point (\[xi, yi, zi])

<!-- @since:5.0.1 -->
### 3. Double

Mirror offset value

<!-- @since:5.0.1 -->
### 4. Bool

Create new part bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 5. Bool

LBC Copy bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 6. Bool

Copy property info bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 7. Bool

Remove duplicate faces bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 8. Bool

Equivalence nodes bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 9. Double

Equivalence nodes tolerance value

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MirrorBody([3:2], [[0, 0.004999999888241291, 0], [0.004999999888241291, 0.004999999888241291, 0],
    [0, 0, 0]], 0.002, 1, 0, 0, 0, 0, 1e-08)
```
