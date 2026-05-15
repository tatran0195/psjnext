---
title: "CmdPlotStrainGaugeNodePoint()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Import

## Syntax

```psj
CmdPlotStrainGaugeNodePoint(cursor PostJob, int node, float[] point, vector[] Steps, string AxisXName, string AxisYName, float Height, float Width, float Factor, bool MaxPrincipal, int nPhaseType, float PhaseAngle, bool CreateMarkup)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. cursor

Post Job

<!-- @since:5.0.1 -->
### 2. int

ID of node.

<!-- @since:5.0.1 -->
### 3. float\[]

Position vector \[x,y,z]

<!-- @since:5.0.1 -->
### 4. vector\[]

Step information vector.

<!-- @since:5.0.1 -->

#### 1. int

Analysis type

<!-- @since:5.0.1 -->

#### 2. int

Result set

<!-- @since:5.0.1 -->

#### 3. int

Time Step

<!-- @since:5.0.1 -->
### 5. string

Name of X Axis.

<!-- @since:5.0.1 -->
### 6. string

Name of Y Axis.

<!-- @since:5.0.1 -->
### 7. float

Gauge - Length

<!-- @since:5.0.1 -->
### 8. float

Gauge - Width

<!-- @since:5.0.1 -->
### 9. float

Gauge - Amend Factor

<!-- @since:5.0.1 -->
### 10. bool

Direction

<!-- @since:5.0.1 -->
### 11. int

Phase Setting - Phase

<!-- @since:5.0.1 -->
### 12. float

Phase Setting - Angle

<!-- @since:5.0.1 -->
### 13. bool

Add Note flag

## Return Code

Nothing.

## Sample Code

```psj
CmdPlotStrainGaugeNodePoint(183:1, 10361, [-0.00216074,-0.00044453,0.000788983], [[2,1,1], [2,1,2], [2,1,4], [2,1,6], [2,1,10]], "Time/Freq(Default)", "Stress(Node)", 0.003, 0.003, 1, -1, 0.000000, 1)
```
