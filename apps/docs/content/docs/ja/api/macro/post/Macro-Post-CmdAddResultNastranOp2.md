---
title: "CmdAddResultNastranOp2()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add nastran result to current model.

## Syntax

```psj
CmdAddResultNastranOp2(cursor postJob, string[] FilePath, int solverType, int offsetID, bool CreateAtMidNodes)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. cursor

Post job.

<!-- @since:5.0.1 -->
### 2. string\[]

File paths

<!-- @since:5.0.1 -->
### 3. int

Solver type

<!-- @since:5.0.1 -->
### 4. int

Offset ID

<!-- @since:5.0.1 -->
### 5. bool

Create at mid nodes option flag.

## Return Code

Nothing.

## Sample Code

```psj
CmdAddResultNastranOp2(183:1, ["C:/Users/TechnoStar/Documents/TSData/11 _Desktop/Solver/boltconnection _converted _bar-fix.op2"], 1, 1, 0)
```
