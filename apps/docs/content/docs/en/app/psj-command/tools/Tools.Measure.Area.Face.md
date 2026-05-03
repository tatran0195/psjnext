---
title: "Tools.Measure.Area.Face()"
description: "Measure an area of a face or a total area of faces"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > Measure > Area > Face"
---

## Description

Measure an area of a face or a total area of faces.

## Syntax

```psj
Tools.Measure.Area.Face(...)
```

## Inputs

### `crlFaces` @type(List\[Cursor]) @required

- The list of faces to measure area.

### `iPrecision` @type(Integer) @default(6)

- The number of digit after floating point. The greater`iPrecision`could be, the more accuracy of Area can be measured.

## Return Code

A _Double_ specifying the area value of a face or a total area value of faces.

## Sample Code

```psj {3}
Geometry.Part.Cube()

area = Tools.Measure.Area.Face(crlFaces=[Face(26)])

JPT.Debugger(area)
```
