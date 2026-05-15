---
title: "PostCreateGraph()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Invert hide targets by context menu

## Syntax

```psj
PostCreateGraph(cursor TargetCurve, int NumData, string LineTitle, double[] AxisDataX, double[] AxisDataY, string ChartTitle, string AxisTitleX, string AxisTitleY, bool NewChart)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Cursor

A Cursor specifying the curve target.

<!-- @since:5.1.0 -->
### 2. Int

An Integer specifying the number of data.

<!-- @since:5.1.0 -->
### 3. String

A String specifying the line title.

<!-- @since:5.1.0 -->
### 4. Double\[]

A Double List specifying data of axis X.

<!-- @since:5.1.0 -->
### 5. Double\[]

A Double List specifying data of axis Y.

<!-- @since:5.1.0 -->
### 6. String

A String specifying the chart title.

<!-- @since:5.1.0 -->
### 7. String

A String specifying the axis X title.

<!-- @since:5.1.0 -->
### 8. String

A String specifying the axis Y title.

<!-- @since:5.1.0 -->
### 9. Bool

A Boolean specifying whether to create new chart.

## Return Code

- "1": The function can be executed.
- "0": The function cannot be executed.

## Sample Code

```psj
PostCreateGraph(3:1,1,"",[0.0,1.0],[1.0,2.0],"","","",True)
```
