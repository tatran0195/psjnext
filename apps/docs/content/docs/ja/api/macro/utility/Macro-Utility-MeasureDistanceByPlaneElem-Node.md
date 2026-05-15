---
title: "MeasureDistanceByPlaneElem _Node()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Measure Distance between Node and plane (created by element).

## Syntax

```psj
MeasureDistanceByPlaneElem _Node(cursor node,cursor edge,Integer N)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor

node cursor(10:_,_=node id)

<!-- @since:5.0.1 -->
### 2. Cursor

edge cursor(11:_,_=edge id)

<!-- @since:5.0.1 -->
### 3. Integer N

specify the number of decimal places (0{'<='}N{'<='}30)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MeasureDistanceByPlaneElem _Node(10:438,11:362,6)
```
