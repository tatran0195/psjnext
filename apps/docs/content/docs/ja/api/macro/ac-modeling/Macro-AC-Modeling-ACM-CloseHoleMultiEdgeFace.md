---
title: "ACM _CloseHoleMultiEdgeFace()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

ACM\_CloseHole\_MultiEdgeFace

## Syntax

```psj
ACM _CloseHoleMultiEdgeFace(cursor[] FaceCursor, cursor[] EdgeCursor, bool bNewBody,
    string newBodyname, bool bRemesh, double dAvgMeshSize)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Face List

<!-- @since:5.0.1 -->
### 2. Cursor\[]

Edge List

<!-- @since:5.0.1 -->
### 3. Bool

Create New Body

<!-- @since:5.0.1 -->
### 4. string

New Body Name

<!-- @since:5.0.1 -->
### 5. Bool

Remesh

<!-- @since:5.0.1 -->
### 6. Double

Average Remesh Size

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CloseHoleMultiEdgeFace([6:13049, 6:13059], [5:290520], 1, "NewBody", 1, 0.008)
```
