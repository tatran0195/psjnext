---
title: "NodeMovedByDirection()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Move node(s) in a specified direction

## Syntax

```psj
NodeMovedByDirection(Cursor[] crNode, Cursor crElem, Cursor crFace, double[3] vctDirection,
    double dMoveAmount, bool BDestiByFaceOrElem)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target node cursor(\[10:Node ID])

<!-- @since:5.0.1 -->
### 2. Cursor

Target element cursor(11:Elem ID)

<!-- @since:5.0.1 -->
### 3. Cursor

Target face cursor(6:Face ID)

<!-- @since:5.0.1 -->
### 4. Double\[3]

Vector direction DX, DY, DZ

<!-- @since:5.0.1 -->
### 5. Double

Move amount user input

<!-- @since:5.0.1 -->
### 6. Bool

Destination by face or element bool flag True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
NodeMovedByDirection([10:1420], 11:3167, 6:78, [0.196116135138184, 0.98058067569092, 0], 0.005, 1)
```
