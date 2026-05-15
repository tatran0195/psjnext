---
title: "MeasureAngleBy2Axis()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Measure the angle created by 2 Axis.

## Syntax

```psj
MeasureAngleBy2Axis(Axis xyz1,Axis xyz2,String Target,Integer N)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Axis

unit vector(\[x,y,z])

<!-- @since:5.0.1 -->
### 2. Axis

unit vector(\[x,y,z])

<!-- @since:5.0.1 -->
### 3. String

Target (Angle or XY or YZ or ZX or ALL)

<!-- @since:5.0.1 -->
### 4. Integer N

specify the number of decimal places (0{'<='}N{'<='}30)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MeasureAngleBy2Axis([0,0,1],[1,1,1],"ALL",6)
```

or

```psj
MeasureAngleBy2Axis([0,0,1],[1,1,1],"Angle",6)
```
