---
title: "MeshEditMoveNodeDeform()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Move nodes deform

## Syntax

```psj
MeshEditMoveNodeDeform(int m _solverType,String m _strFilePath,int m _iStep,double m _dScale)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int

type of solver

<!-- @since:5.0.1 -->
### 2. String

file path

<!-- @since:5.0.1 -->
### 3. Int

Step

<!-- @since:5.0.1 -->
### 4. Double

value of scale

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MeshEditMoveNodeDeform(1,"Test",1,0.001)
```
