---
title: "AddItemsEdgeProjectEdgetoFace()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add Items Edge by Projecting Edge to Face with smallest distance

## Syntax

```psj
AddItemsEdgeProjectEdgetoFace(int[] FaceKey, int[] EdgeKey, bool ExtendToEdge)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int\[]

Target Faces for projecting Edge

<!-- @since:5.0.1 -->
### 2. Int\[]

Target Edge to be projected

<!-- @since:5.0.1 -->
### 3. Bool

Extend the Newly Created Edge up to Nearby Edges. true = 1,false = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
AddItemsEdgeProjectEdgetoFace([24], [42], 1)
```
