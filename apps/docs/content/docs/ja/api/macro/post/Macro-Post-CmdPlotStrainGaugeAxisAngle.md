---
title: "CmdPlotStrainGaugeAxisAngle()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Import

## Syntax

```psj
CmdPlotStrainGaugeAxisAngle(cursor PostJob, vector[] Steps, int[] nodes, int Axis1, int Axis2, float Angle, string AxisXName, string AxisYName, float Height, float Width, float Factor, int nPhaseType, float PhaseAngle, bool CreateMarkup)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. cursor

Post Job

<!-- @since:5.0.1 -->
### 2. vector\[]

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
### 3. int\[]

Target node IDs.

<!-- @since:5.0.1 -->
### 4. int

First Axis

<!-- @since:5.0.1 -->
### 5. int

Second Axis

<!-- @since:5.0.1 -->
### 6. float

Angle.

<!-- @since:5.0.1 -->
### 7. string

Name of X Axis.

<!-- @since:5.0.1 -->
### 8. string

Name of Y Axis.

<!-- @since:5.0.1 -->
### 9. float

Gauge - Length

<!-- @since:5.0.1 -->
### 10. float

Gauge - Width

<!-- @since:5.0.1 -->
### 11. float

Gauge - Amend Factor

<!-- @since:5.0.1 -->
### 12. int

Phase Setting - Phase

<!-- @since:5.0.1 -->
### 13. float

Phase Setting - Angle

<!-- @since:5.0.1 -->
### 14. bool

Add Note flag

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 1. string

Post Job

## Return Code

Nothing.

## Sample Code

```psj
CmdPlotStrainGaugeAxisAngle(183:1, [[2,1,1], [2,1,2], [2,1,3], [2,1,4], [2,1,5], [2,1,6], [2,1,7], [2,1,8], [2,1,9], [2,1,10]], [2828], 0, 1, 30.000000, "Time/Freq(Default)", "Stress(Node)", 0.003, 0.003, 1, -1, 0.000000, 1)
```
