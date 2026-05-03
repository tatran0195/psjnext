---
title: "Geometry.MergeEntities.Edges()"
description: "Merge all the selected edges into uninterrupted edges"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Merge Entities > Edges"
---

## Description

Merge all the selected edges into uninterrupted edges.

## Syntax

```psj
Geometry.MergeEntities.Edges(...)
```

## Inputs

### `crlEdges` @type(List\[Cursor]) @required

- The edges to be merged.

## Return Code

A _List of Cursor_ specifying the merged edges.

## Sample Code

```psj {4,5,6,7,8,9,10,11,12,13,14,15,16,17,18}
Geometry.Part.Cube()
Geometry.BreakEntity.Edge(crlNodes=[Node(95, 92, 90)])

merged_edges = Geometry.MergeEntities.Edges(crlEdges=[Edge(9, 
                                                           10, 
                                                           11, 
                                                           12, 
                                                           13, 
                                                           14, 
                                                           15, 
                                                           16, 
                                                           17, 
                                                           18, 
                                                           20, 
                                                           28, 
                                                           32, 
                                                           34, 
                                                           35)])

JPT.Debugger(merged_edges)
```
