---
title: "Tools.Measure.Area.Face()"
description: "Measure an area of a face or a total area of faces"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > Measure > Area > Face"
---

## Description

Measure an area of a face or a total area of faces.

## Syntax

```psj
Tools.Measure.Area.Face(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlFaces`

- The list of faces to measure area.

<!-- @since:5.0.1 @type:Integer @optional @default:6 -->
### `iPrecision`

- The number of digit after floating point. The greater`iPrecision` could be, the more accuracy of Area can be measured.

## Return Code

A _Double_ specifying the area value of a face or a total area value of faces.

## Sample Code

```psj {3}
Geometry.Part.Cube()

area = Tools.Measure.Area.Face(crlFaces=[Face(26)])

JPT.Debugger(area)
```
