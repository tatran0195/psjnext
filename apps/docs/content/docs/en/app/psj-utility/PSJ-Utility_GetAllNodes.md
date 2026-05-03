---
title: "JPT.GetAllNodes()"
description: "Get all the information of all existing nodes"
version_introduced: "5.0.1"
available_versions: "all"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Get all the information of all existing nodes.

:::note

If this function is executed on a Post document, it returns 0. If you want to get all Post nodes, please use  _[GetAllPostNodes](JPT.GetAllPostNodes)_.

:::

## Syntax

```psj
JPT.GetAllNodes()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _[NodeVector](../data-type/psj-utility/pre-utility/built-in-types/NodeVector)_ object or _List of [DNode](../data-type/psj-utility/pre-utility/built-in-types/DNode)_ objects containing all the information of all the existing nodes.

## Sample Code

```psj {8}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Get the information of all existing nodes
listDNodes = JPT.GetAllNodes()
JPT.Debugger(listDNodes)

# Print all the related information of each existing node in list
for node in listDNodes:
    JPT.Debugger(node)
```
