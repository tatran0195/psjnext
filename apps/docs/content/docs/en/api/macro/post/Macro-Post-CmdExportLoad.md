---
title: "CmdExportLoad()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Export Load as file.

## Syntax

```psj
CmdExportLoad(cursor[] taEntity, int analysisType, int resultSet, int timeStep, vecResultLoad [] ResultLoads, int SolverType, string ExportFile)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. cursor\[]

Target entity.

<!-- @since:5.0.1 -->
### 2. int

Analysis type.

<!-- @since:5.0.1 -->
### 3. int

Result set.

<!-- @since:5.0.1 -->
### 4. int

Time step.

<!-- @since:5.0.1 -->
### 5. ResultLoad \[]

ResultLoad consisted by:

1. vrType - vr type,
1. string - Result name,
1. string - Load name.

<!-- @since:5.0.1 -->

#### 6. int

Solver type.

<!-- @since:5.0.1 -->

#### 7. string

Exported file name.

## Return Code

Nothing.

## Sample Code

```psj
CmdExportLoad([10:1008], 1,1,1, [[6, Displacement,Initial Displacement]], 2, "C:/Temp/data.dat")
```
