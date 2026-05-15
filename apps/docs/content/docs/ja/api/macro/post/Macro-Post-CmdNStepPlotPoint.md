---
title: "CmdNStepPlotPoint()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Execute N-Step Plot (Position)

## Syntax

```psj
CmdNStepPlotPoint(cursor PostJob, FacePointItem [] item, stepItem [] item, bool CreateMarkup, string XResult, string XComponent, int XLoc)
```

## Inputs

3-6 are a set of a position list.
7-9 are a set of a plot target list.

<!-- @since:5.0.1 -->
### 1. cursor

Post job.

<!-- @since:5.0.1 -->
### 2. FacePointItem\[]

List of item Consist of:

- int : Element ID where the face point belongs to.
- float : X position of the face point.
- float : Y position of the face point.
- float : Z position of the face point.

<!-- @since:5.0.1 -->
### 3. stepItem \[]

List of item Consist of:

- int : Analysis type
- int : Result set
- int : timeStep

<!-- @since:5.0.1 -->
### 4. float

Create notes on Elements or not

<!-- @since:5.0.1 -->
### 5. string

X Axis Data - Result.

<!-- @since:5.0.1 -->
### 6. int

X Axis Data - Component

<!-- @since:5.0.1 -->
### 7. int

X Axis Data - Data Location

## Return Code

Nothing.

## Sample Code

```psj
CmdNStepPlotPoint(183:1, [[2603, 10.427549, -0.598614, 13.343364],[2615, 10.235324, -1.799746, 12.080006],[2666, 9.768378, 3.305036, 14.630617]], [[1,0,0], [1,1,5], [1,2,5], [1,3,5], [1,4,5]], 1)
```
