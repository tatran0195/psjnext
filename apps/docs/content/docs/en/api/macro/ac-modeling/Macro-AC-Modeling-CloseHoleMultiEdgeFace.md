---
title: "CloseHoleMultiEdgeFace()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

CloseHoleMultiEdgeFace

## Syntax

```psj
CloseHoleMultiEdgeFace(cursor[] crBody, cursor[] crFace, cursor[] crEdge, bool bSelBelPart,
    bool SpecPart, bool bNewPart, string strName, bool bRemesh, double dElemSize))
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target body cursor(\[3:Body ID])

<!-- @since:5.0.1 -->
### 2. Cursor\[]

Target face cursor(\[6:Face ID])

<!-- @since:5.0.1 -->
### 3. Cursor\[]

Target edge cursor(\[5:Edge ID])

<!-- @since:5.0.1 -->
### 4. Bool

Select belong part bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 5. Bool

Specified part bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 6. Bool

New part bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 7. String

New part name

<!-- @since:5.0.1 -->
### 8. Bool

Remesh bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 9. Double

Element size

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CloseHoleMultiEdgeFace([], [6:62], [5:10000162, 5:10000153], 0, 0, 0, "", 1, 0.008)
```
