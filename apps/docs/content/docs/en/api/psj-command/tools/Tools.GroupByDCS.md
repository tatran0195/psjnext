---
title: "Tools.GroupByDCS()"
description: "Create node groups according to the nodal coordinate system."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > GroupByDCS"
---

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

```psj {22}
#Prepare model
Geometry.Part.Cube(
    ilAxialNodes=[4, 4, 4], 
    iPartColor=7463537)
Tools.Coordinates.Face(
    strName="CRect _4", 
    veclPoint=[[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], 
    crItem=Face(24))

#Find target face
faces=JPT.Exec('FindEntities("-10,5,5","Face", 0)')

#Get ids from the result and input into Face function.

ditem _list=JPT.MacroListTCursorToListDItem(faces)
ids=[ditem.id for ditem in ditem _list]

#Create nodal coordinate system for the nodes in the selected face. 
Tools.DisplacementCS(crlInst=[Face(*ids)], crCoordSystem=Coord(1))

#Create node groups according to the nodal coordinate system.
Tools.GroupByDCS()
```
