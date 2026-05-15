---
title: "CmdMaxMinPlot()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Execute Max/Min Plot

## Syntax

```psj
CmdMaxMinPlot(PostStepItem[] vecStep, bool ExportCsv, string File )
```

## Inputs

<!-- @since:5.0.1 -->
### 1. PostStepItem\[]

List of results to plot. int analysisType, int resultSet, int timeStep

<!-- @since:5.0.1 -->
### 2. bool

Flag of Export CSV File.

<!-- @since:5.0.1 -->
### 3. string

Path of CSV file.

## Return Code

Nothing.

## Sample Code

```psj
CmdMaxMinPlot([[1,0,0], [1,0,1], [1,0,2], [1,0,3], [1,0,4], [1,0,5], [1,0,6], [1,0,7], [1,0,8], [1,0,9]], 0, "")
```
