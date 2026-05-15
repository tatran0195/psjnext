---
title: "PostCreateGraph()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create graph.

## Syntax

```psj
PostCreateGraph(cursor RefAnalysis, int np, string curveTitle, float[] xpos, float[] ypos, string graphTitle, string XAxisTitle, string YAxisTitle, bool newChart)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. cursor

Frequency analysis' cursor. If here is not 0:0, from 2 to 5 are omitted.

<!-- @since:5.0.1 -->
### 2. int

The number of plot point.

<!-- @since:5.0.1 -->
### 3. string

Curve title.

<!-- @since:5.0.1 -->
### 4. float\[]

X positions.

<!-- @since:5.0.1 -->
### 5. float\[]

Y positions.

<!-- @since:5.0.1 -->
### 6. string

Graph title.

<!-- @since:5.0.1 -->
### 7. string

X axis title.

<!-- @since:5.0.1 -->
### 8. string

Y axis title.

<!-- @since:5.0.1 -->
### 9. bool

Create a new chart flag.

## Return Code

Nothing.

## Sample Code

```psj
PostCreateGraph(0:0, 5, "Curve Title", [0, 3, 5, 7, 10], [0, 1, 2, 5, 20], "Main Title", "X Axis Title", "Y Axis Title", 0)
PostCreateGraph(196:1, "Frequency Analysis Displacement", "Frequency", "Amplitude", 1)
```
