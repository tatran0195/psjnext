---
title: "MeasureDistanceByEdge _Node()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Measure the distance between the Edge and the Note

## Syntax

```psj
MeasureDistanceByEdge _Node(cursor edge,cursor node,Integer N)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor

edge cursor(5:_,_=edge id)

<!-- @since:5.0.1 -->
### 2. Cursor

node cursor(10:_,_=node id)

<!-- @since:5.0.1 -->
### 3. Integer N

specify the number of decimal places (0{'<='}N{'<='}30)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MeasureDistanceByEdge _Node(5:18,10:459,6)
```
