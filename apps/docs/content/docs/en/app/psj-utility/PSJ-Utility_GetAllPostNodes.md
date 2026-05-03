---
title: "JPT.GetAllPostNodes()"
description: "Get all the information of all existing Post (read-only) nodes"
version_introduced: "5.1.0"
available_versions: "all"
---

## Description

Get all the information of all existing Post (read-only) nodes.

:::note

If this function is executed on a Pre document, it returns 0. If you want to get all pre nodes, please use  _[GetAllNodes](JPT.GetAllNodes)_.

:::

## Syntax

```psj
JPT.GetAllPostNodes()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _[PostNodeVector](../data-type/psj-utility/post-utility/post-built-in-types/PostNodeVector)_ object or _List of [DPostNode](../data-type/psj-utility/post-utility/post-built-in-types/DPostNode)_ objects containing all the information of all the existing nodes.

## Sample Code

```psj {11}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Displacement, X, 1}, {1, 1, 0, \
                             0, 0, 0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, \
                             {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, \
                             {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, 0)')

# Get the result values of Nodes
for postNode in JPT.GetAllPostNodes():
    value=JPT.GetResultByNodeId(postNode.id)
    print(f"Displacement of X component of Node ID = {postNode.id}:{value}")
```
