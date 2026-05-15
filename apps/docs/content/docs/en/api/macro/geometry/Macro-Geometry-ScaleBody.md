---
title: "ScaleBody()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Scale Body

## Syntax

```psj
ScaleBody(cursor[] taBody, double[3] scaleVector, double[3] scaleCentre, cursor crCoord,
    bool createNew, bool copyLBC, bool usePartCenter)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target part cursor(\[3:Part ID])

<!-- @since:5.0.1 -->
### 2. Double\[3]

Scale vector(x, y, z)

<!-- @since:5.0.1 -->
### 3. Double\[3]

Scale center(x, y, z)

<!-- @since:5.0.1 -->
### 4. Cursor

Whether use local coordinate or not True = 27:\*, False = 0:0

<!-- @since:5.0.1 -->
### 5. Bool

Create new part bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 6. Bool

LBC copy bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 7. Bool

Use part center bool flag True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ScaleBody([3:1], [1, 5, 1], [0, 0, 0], 0:0, 1, 0, 1)
```
