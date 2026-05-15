---
title: "MeasureAngleBy2Nodes _Axis()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Measure the angle created by 2 nodes and Axis.

## Syntax

```psj
MeasureAngleBy2Nodes _Axis(cursor node1,cursor node2,Axis xyz,String Target,Integer N)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor

node cursor(10:_;_=node id)

<!-- @since:5.0.1 -->
### 2. Cursor

node cursor(10:_;_=node id)

<!-- @since:5.0.1 -->
### 3. Axis

unit vector(\[x,y,z])

<!-- @since:5.0.1 -->
### 4. String

Target (Angle or XY or YZ or ZX or ALL)

<!-- @since:5.0.1 -->
### 5. Integer N

specify the number of decimal places (0{'<='}N{'<='}30)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MeasureAngleBy2Nodes _Axis(10:331,10:323,[0,0,1],"ALL",6)
```

or

```psj
MeasureAngleBy2Nodes _Axis(10:331,10:323,[0,0,1],"Angle",6)
```
