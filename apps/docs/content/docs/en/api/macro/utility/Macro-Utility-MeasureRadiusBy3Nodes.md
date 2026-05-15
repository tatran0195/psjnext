---
title: "MeasureRadiusBy3Nodes()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Measure the angle created by 3 nodes.

## Syntax

```psj
MeasureRadiusBy3Nodes(cursor node1,cursor node2,cursor node3,Integer N)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. cursor

node1 cursor(10:_,_=node id)

<!-- @since:5.0.1 -->
### 2. cursor

node2 cursor(10:_,_=node id)

<!-- @since:5.0.1 -->
### 3. cursor

node3 cursor(10:_,_=node id)

<!-- @since:5.0.1 -->
### 4. Integer N

specify the number of decimal places (0{'<='}N{'<='}30)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MeasureRadiusBy3Nodes(10:16,10:2,10:58,6)
```
