---
title: "CmdAddResultTSVPost()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add result to current mesh data.

## Syntax

```psj
CmdAddResultTSVPost(cursor Job, string[] path, int solverType, int offsetID)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. cursor

Post job.

<!-- @since:5.0.1 -->
### 2. string\[]

File paths.

<!-- @since:5.0.1 -->
### 3. int

_[Solver type](../../data-type/psj-utility/post-utility/enumeration-types/post-job-type.md)_.

<!-- @since:5.0.1 -->

#### 4. int

Offset ID.

## Return Code

Nothing.

## Sample Code

```psj
CmdAddResultTSVPost(183:1, ["C:/temp/data.unv"], 4, 1)
```
