---
title: "MoveNodeAbsolute()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Move node(s) to an absolute position

## Syntax

```psj
MoveNodeAbsolute(double dDeltaX, double dDeltaY, double dDeltaZ, bool b1stCoord,
    bool b2ndCoord, bool b3rdCoord, int[] taNodeKey, cursor crCoord)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Double

X coordinate to move the node

<!-- @since:5.0.1 -->
### 2. Double

Y coordinate to move the node

<!-- @since:5.0.1 -->
### 3. Double

Z coordinate to move the node

<!-- @since:5.0.1 -->
### 4. Bool

X coordinate bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 5. Bool

Y coordinate bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 6. Bool

X coordinate bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 7. Int\[]

Node key cursor(\[Node ID])

<!-- @since:5.0.1 -->
### 8. Cursor

Whether use local coordinate or not True = 27:\*, False = 0:0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MoveNodeAbsolute(-0.015, 0.015, 0.015, 1, 1, 1, [1069], 0:0)
```
