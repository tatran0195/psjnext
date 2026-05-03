---
title: "JPT.GetSelectedFacesCr()"
description: "Get all information of the selected faces under list of cursor format"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Get all information of the selected faces under _List of Cursor_ format.

## Syntax

```psj
JPT.GetSelectedFacesCr()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _String_ specifying a cursor list (Macro string type) containing typeID and ID of the selected faces.

## Sample Code

```psj {13}
# Prepare model
Geometry.Part.Cube(iPartColor=7138156)
Geometry.Part.Cube(strName="Cube_2", iPartColor=5921475)
Geometry.Part.Cube(strName="Cube_3", iPartColor=6678117)
Geometry.Part.Cube(strName="Cube_4", iPartColor=11908427)
Geometry.Part.Cube(strName="Cube_5", iPartColor=15429611)
Geometry.Part.Cube(strName="Cube_6", iPartColor=7531634)
Geometry.Part.Cube(strName="Cube_7", iPartColor=12434775)
Home.Find(strSearch="20 21 22 23 24", strSelectedType="Face")
JPT.ViewFitToModel()

# Get the information of all selected edges
listCursorSelFaces = JPT.GetSelectedFacesCr()
JPT.Debugger(listCursorSelFaces)
```
