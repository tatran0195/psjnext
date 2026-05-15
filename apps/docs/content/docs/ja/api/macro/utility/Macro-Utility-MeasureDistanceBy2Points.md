---
title: "MeasureDistanceBy2Points()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Measure the distance between two points

## Syntax

```psj
MeasureDistanceBy2Points(Point[] xyz,String Target,Integer N)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Points\[]

Point xyz Coordinate(\[\[x1,y1,z1],\[x2,y2,z2]])

<!-- @since:5.0.1 -->
### 2. String

Target(Dist or X or Y or Z or ALL)

<!-- @since:5.0.1 -->
### 3. Integer N

specify the number of decimal places (0{'<='}N{'<='}30)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MeasureDistanceBy2Points([[0.0066666,0.00333333,0.01],[0.004444440.0077777,0.01]],"X",6)
```

or

```psj
MeasureDistanceBy2Points([[0.0066666,0.00333333,0.01],[0.004444440.0077777,0.01]],"Dist",6)
```
