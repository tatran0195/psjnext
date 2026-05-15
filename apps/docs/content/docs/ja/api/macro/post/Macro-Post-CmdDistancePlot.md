---
title: "CmdDistancePlot()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Distance Plot.

## Syntax

```psj
CmdDistancePlot(int Node1, int Node2, PostStepItem [] stepItem, bool DistXYZ, bool PosXYZ )
```

## Inputs

<!-- @since:5.0.1 -->
### 1. int

Node 1 ID

<!-- @since:5.0.1 -->
### 2. int

Node 2 ID

<!-- @since:5.0.1 -->
### 3. PostStepItem \[]

Source results.

PostStepItems are:

1. int - Analysis type.
1. int - Result set.
1. int - Time step.

<!-- @since:5.0.1 -->
### 4. bool

X, Y, Z Distance Plot flag.

<!-- @since:5.0.1 -->
### 5. bool

X, Y, Z Position Plot flag.

## Return Code

Nothing.

## Sample Code

```psj
CmdDistancePlot(8, 2, [[1,0,0], [1,0,1], [1,0,2], [1,0,3]], 0, 1)
```
