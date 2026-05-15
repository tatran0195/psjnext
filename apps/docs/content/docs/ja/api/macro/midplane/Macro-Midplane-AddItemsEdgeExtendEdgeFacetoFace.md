---
title: "AddItemsEdgeExtendEdgeFacetoFace()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add Items Edge by projecting Edge on to the intersecting point of Face

## Syntax

```psj
AddItemsEdgeExtendEdgeFacetoFace(cursor[] Edge, cursor[] Face, bool Neighbour Edge Direction,
    bool Project to connect Faces)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor \[]

Target edge to be projected

<!-- @since:5.0.1 -->
### 2. Cursor \[]

Target Faces for projecting Edge

<!-- @since:5.0.1 -->
### 3. Bool

Create the New Edge at the intersecting point of projected Edge's neighbour edges on the Face true = 1,false = 0

<!-- @since:5.0.1 -->
### 4. Bool

Create the New Edge on connected Faces of the Target Face. true = 1,false = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
AddItemsEdgeExtendEdgeFacetoFace([5:31], [6:24], 1, 0)
```
