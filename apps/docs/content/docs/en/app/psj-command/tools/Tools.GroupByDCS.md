---
title: "Tools.GroupByDCS()"
description: "Create node groups according to the nodal coordinate system."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > GroupByDCS"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Unknown Description","Create node groups according to the nodal coordinate system."]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create node groups according to the nodal coordinate system.

## Syntax

```psj
Tools.GroupByDCS()
```

## Inputs

None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj{22}
#Prepare model
Geometry.Part.Cube(
    ilAxialNodes=[4, 4, 4], 
    iPartColor=7463537)
Tools.Coordinates.Face(
    strName="CRect_4", 
    veclPoint=[[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], 
    crItem=Face(24))

#Find target face
faces=JPT.Exec('FindEntities("-10,5,5","Face", 0)')

#Get ids from the result and input into Face function.

ditem_list=JPT.MacroListTCursorToListDItem(faces)
ids=[ditem.id for ditem in ditem_list]

#Create nodal coordinate system for the nodes in the selected face. 
Tools.DisplacementCS(crlInst=[Face(*ids)], crCoordSystem=Coord(1))

#Create node groups according to the nodal coordinate system.
Tools.GroupByDCS()
```
