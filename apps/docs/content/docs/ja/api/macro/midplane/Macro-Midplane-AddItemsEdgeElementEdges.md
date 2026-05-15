---
title: "AddItemsEdgeElementEdges()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add Items Edge from Element Edges

## Syntax

```psj
AddItemsEdgeElementEdges(elemEdge[] ElemEdge, bool BreakFace)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. ElemEdge \[]

Target Element Edges for Creating New Edge

<!-- @since:5.0.1 -->
### 2. Bool

Break Face. true = 1,false = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CreateEdgeByElemEdge([10:172-10:180, 10:180-10:188, 10:188-10:196], 1)
```
