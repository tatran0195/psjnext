---
title: "ModelInfo()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get Model Information from Target String

## Syntax

```psj
ModelInfo(Target String) or ModelInfo(Target String,Name String)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Target String(bodyNum,faceNum,edgeNum,vertexNum, surfaceNodeNum,solidNodeNum,surfaceElemNum,solidElemNum, tri3ElemNum,tri6ElemNum,quad4ElemNum,quad8ElemNum, tet4ElemNum,tet10ElemNum,hex8ElemNum,hex20ElemNum,penta5ElemNum,penta6ElemNum,penta15ElemNum,pyramid13ElemNum or coordinateByName,loadCaseByName,materialByName,bodyByName,LBCByName,AbaqusStepByName,PropertyByName,GroupByName)

<!-- @since:5.0.1 -->
### 2. String

Name

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ModelInfo("surfaceElemNum")
```

or

```psj
ModelInfo("coordinateByName","aaaa")
```
