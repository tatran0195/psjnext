---
title: "CmdImportTSVOp2Post()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Import Nastran .op2 result file

## Syntax

```psj
CmdImportTSVOp2Post(string FilePath, int importType, float faceAngle, float edgeAngle, bool readLoadAndConst, bool readConnection bool createResultsAtMidNode)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. string

File path

<!-- @since:5.0.1 -->
### 2. int

Import Type
0: Simple Topology
1: Standard Nastran Op2 by Property

<!-- @since:5.0.1 -->
### 3. float

Face Angle

<!-- @since:5.0.1 -->
### 4. float

Edge Angle

<!-- @since:5.0.1 -->
### 5. bool

Read Load and Constraint flag

<!-- @since:5.0.1 -->
### 6. bool

Read Connection flag

<!-- @since:5.0.1 -->
### 6. bool

Create Results at Mid Nodes flag

## Return Code

Nothing.

## Sample Code

```psj
CmdImportTSVOp2Post("C:/temp/data.op2", 1, 1.0472, 1.0472, 0, 0, 0)
```
