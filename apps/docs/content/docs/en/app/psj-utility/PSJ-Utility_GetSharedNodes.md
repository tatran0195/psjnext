---
title: "JPT.GetSharedNodes()"
description: "Get all information of the shared nodes"
version_introduced: "5.0.1"
available_versions: "all"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Get all information of the shared nodes.

## Syntax

```psj
JPT.GetSharedNodes(DItemVector)
```

## Inputs

### `DItemVector` @type(DItemVector) @required

- Object o&#x72;_&#x4C;ist of[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_&#x6F;bjects to get the shared nodes.

## Return Code

A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects containing all the information of all the shared nodes.

## Sample Code

```psj {14}
# Prepare model
Geometry.Part.Cube(iPartColor=6217822)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6908379)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=7138924)
Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0], strName="Cube_4", iPartColor=15753968)
JPT.ViewFitToModel()

# Create shared faces
JPT.Exec('AssembleFaceMatingStep([], [], [3:1, 3:2, 3:3, 3:4], 1e-05)')
JPT.Exec('AssembleFaceEx([49, 24, 50, 75, 101, 76], 1e-05, 0, 0)')

# Get the information of all shared nodes
listParts = JPT.GetAllByTypeID(JPT.DItemType.BODY)
listSharedNodes = JPT.GetSharedNodes(listParts)
JPT.Debugger(listSharedNodes)
```
