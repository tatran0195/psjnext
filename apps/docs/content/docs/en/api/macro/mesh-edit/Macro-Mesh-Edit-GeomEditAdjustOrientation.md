---
title: "GeomEditAdjustOrientation()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Adjust Orientation

## Syntax

```psj
GeomEditAdjustOrientation(cursor[] taBody, cursor[] taFace, cursor[] taElem)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target body cursor(\[3:Part ID])

<!-- @since:5.0.1 -->
### 2. Cursor\[]

Target face cursor(\[6:Face ID])

<!-- @since:5.0.1 -->
### 3. Cursor\[]

Target element cursor(\[11:Elem ID])

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
GeomEditAdjustOrientation([], [6:40], [11:182])
```
