---
title: "CmdExportLoad()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Export the selected result name to solver information (as solver keyword card) for the selected entities. Depending on selection of convert load type, the analysis result will be exported to solver card information respectively.

## Syntax

```psj
CmdExportLoad(cursor[] Targets, int AnalysisType, int ResultSet, int TimeStep, vector ResultLoad, int SolverType, string ExportPath)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. cursor\[]

A Cursor List specifying the selected entities.

<!-- @since:5.1.0 -->
### 2. int

Choose type of analysis.

<!-- @since:5.1.0 -->
### 3. int

An Integer specifying the set of results.

<!-- @since:5.1.0 -->
### 4. int

An Integer specifying the time step.

<!-- @since:5.1.0 -->
### 5. vector

A Vector of _[RESULT\_LOAD](../../data-type/psj-command/parameter-types/RESULT _LOAD)_ specifying the components of the selected result.

<!-- @since:5.1.0 -->
### 6. int

An Integer specifying the solver type.

<!-- @since:5.1.0 -->
### 7. string

A String specifying the path of file to be exported.

## Return Code

- "1": The function can be executed.
- "0": The function cannot be executed.

## Sample Code

```psj
CmdExportLoad([3:1,3:2,3:3], 0, 0, 0, [], 2, "C:/temp/ResultToLoadFile")
```
