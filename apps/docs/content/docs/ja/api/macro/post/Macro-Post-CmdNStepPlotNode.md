---
title: "CmdNStepPlotNode()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Execute N-Step Plot (node)

## Syntax

```psj
CmdNStepPlotNode(cursor PostJob, int[] nodes, [int analysisType, int resultSet, int timeStep], bool CreateMarkup, string XResult, string XComponent, int XLoc)
```

## Inputs

3-5 are a set of a plot target list.

<!-- @since:5.0.1 -->
### 1. int

Post job.

<!-- @since:5.0.1 -->
### 2. cursor\[]

List of target nodes

<!-- @since:5.0.1 -->
### 3. int

Analysis type

<!-- @since:5.0.1 -->
### 4. int

Result set

<!-- @since:5.0.1 -->
### 5. int

Time Step

<!-- @since:5.0.1 -->
### 6. bool

Create notes on nodes or not

<!-- @since:5.0.1 -->
### 7. string

X Axis Data - Result.

<!-- @since:5.0.1 -->
### 8. int

X Axis Data - Component

<!-- @since:5.0.1 -->
### 9. int

X Axis Data - Data Location

## Return Code

Nothing.

## Sample Code

```psj
CmdNStepPlotNode(183:1, [988], [[1,0,0], [1,1,5], [1,2,5], [1,3,5], [1,4,5]], 1)
```
