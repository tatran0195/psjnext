---
title: "JPT.GetScreenPositionOfEntities()"
description: "Obtains the position of the specified item in the Main Window."
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Obtains the position of the specified item in the Main Window in screen coordinate system \[min\_x,min\_y,max\_x,max\_y].

## Syntax

```psj
JPT.GetScreenPositionOfEntities(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### DItemVector

- Specify the item whose position on the Main Window is to be retrieved.

## Return Code

A list of\_\[int]\_ representing the upper left and lower right coordinates of the area. If no item found on the Main Window, it returns a blank list.

## Sample Code

```psj {7}
# Prepare model
Geometry.Part.Cube(iPartColor=13290083)
Geometry.Part.Cube(dlOrigin=[0.012, 0.0, 0.0], strName="Cube _2", iPartColor=6149981)
JPT.ViewFitToModel()

# Check screen position of parts in Main Window.
ditem _list=JPT.GetAllByTypeID(JPT.DItemType.BODY)
pos=JPT.GetScreenPositionOfEntities(ditem _list)
JPT.Debugger(pos)
```
