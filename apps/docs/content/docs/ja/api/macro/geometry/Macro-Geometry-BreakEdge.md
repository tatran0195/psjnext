---
title: "BreakEdge()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Break selected edge

## Syntax

```psj
BreakEdge(int[] taBodyKey, int[] taFacekey, int[] taEdgeKey, int[] taNodeKey, bool bAutoByAngle, double dEdgeAngle)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int\[]

Part IDs

<!-- @since:5.0.1 -->
### 2. Int\[]

Face IDs

<!-- @since:5.0.1 -->
### 3. Int\[]

Edge IDs

<!-- @since:5.0.1 -->
### 4. Int\[]

Node IDs

<!-- @since:5.0.1 -->
### 5. Bool

Whether use Auto By Angle True = 1, False = 0

<!-- @since:5.0.1 -->
### 6. Double

Enter edge angle

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
BreakEdge([], [], [], [27169, 27160], 0, 1.0472)
```
