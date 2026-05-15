---
title: "CmdPlotStrainGaugePrincipal()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Strain gauge (Principal)

## Syntax

```psj
CmdPlotStrainGaugePrincipal(cursor PostJob, int[] nodes, vector[] Steps, string AxisXName, string AxisYName, float Height, float Width, float Factor, bool MaxPrincipal, int nPhaseType, float PhaseAngle, bool CreateMarkup)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. cursor

Post Job

<!-- @since:5.0.1 -->
### 2. int\[]

Target node IDs.

<!-- @since:5.0.1 -->
### 3. vector\[]

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
### 4. string

Name of X Axis.

<!-- @since:5.0.1 -->
### 5. string

Name of Y Axis.

<!-- @since:5.0.1 -->
### 6. float

Gauge - Length

<!-- @since:5.0.1 -->
### 7. float

Gauge - Width

<!-- @since:5.0.1 -->
### 8. float

Gauge - Amend Factor

<!-- @since:5.0.1 -->
### 9. bool

Direction

<!-- @since:5.0.1 -->
### 10. int

Phase Setting - Phase

<!-- @since:5.0.1 -->
### 11. float

Phase Setting - Angle

<!-- @since:5.0.1 -->
### 12. bool

Add Note flag

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 1. string

Post Job

## Return Code

Nothing.

## Sample Code

```psj
CmdPlotStrainGaugePrincipal(183:1, [2789], [[2,1,1], [2,1,2], [2,1,3], [2,1,4], [2,1,5], [2,1,6], [2,1,7], [2,1,8], [2,1,9], [2,1,10]], "Time/Freq(Default)", "Stress(Node)", 0.005, 0.005, 1, 1, -1, 0.000000, 1)
```
