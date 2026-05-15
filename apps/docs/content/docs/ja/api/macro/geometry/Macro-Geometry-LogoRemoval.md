---
title: "LogoRemoval()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Face From Edges

## Syntax

```psj
LogoRemoval(cursor[] startFaces, cursor[] stopFaces, int layers, bool mergeFace)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Start faces cursor list (\[6:Face ID])

<!-- @since:5.0.1 -->
### 2. Cursor\[]

End faces cursor list (\[6:Face ID])

<!-- @since:5.0.1 -->
### 3. Int

Layer count of adjacent faces to the start faces

<!-- @since:5.0.1 -->
### 4. Bool

Whether merge face or not True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
LogoRemoval([6:84, 6:77, 6:95, 6:64], [6:2], 5, 0)
```
