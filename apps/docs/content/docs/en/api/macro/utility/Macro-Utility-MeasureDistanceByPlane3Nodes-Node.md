---
title: "MeasureDistanceByPlane3Nodes _Node()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Measure Distance between Node and plane (created by 3 nodes).

## Syntax

```psj
MeasureDistanceByPlane3Nodes _Node(cursor node1,cursor node2,cursor node3,cursor node,Integer N)
```

## Inputs

### \`1. Cursor

node1 cursor(10:_,_=node id)

### \`2. Cursor

node2 cursor(10:_,_=node id)

### \`3. Cursor

node3 cursor(10:_,_=node id)

### \`4. Cursor

node cursor(10:_,_=node id)

<!-- @since:5.0.1 -->
### 5. Integer N

specify the number of decimal places (0{'<='}N{'<='}30)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MeasureDistanceByPlane3Nodes _Node(10:438,10:478,10:450,10:396,6)
```
