---
title: "Geometry.ShowAdjacent.Elements()"
description: "Expand the selection in all directions, regardless of the shape of surrounding features or the angle at which objects are joined. It obtained by recursively finding adjacent elements at an angle of less than or equal to the specified angle"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Show Adjacent > Elements"
---

## Description

Expand the selection in all directions, regardless of the shape of surrounding features or the angle at which objects are joined.
It obtained by recursively finding adjacent elements at an angle of less than or equal to the specified angle.

## Syntax

```psj
Geometry.ShowAdjacent.Elements(...)
```

## Inputs

### `dAngle` @type(Double) @default(0.0)

- The angle between elements in degree. The adjacent elements that are at an angle of less than or equal t&#x6F;_&#x64;Angl&#x65;_&#x77;ill be selected.

### `bIncludeStopElems` @type(Boolean) @default(False)

- Whether to add the stop elements to the selection list or not.

### `iNumOfLayers` @type(Integer) @default(1)

- The number of adjacent layers to be searched.

### `crlStartElems` @type(List\[Cursor]) @default(\[])

- A sequence of the start elements.

### `crlStopElems` @type(List\[Cursor]) @default(\[])

- A sequence of the stop elements.

## Return Code

A _List of Cursor_ specifying a sequence of adjacent elements.

## Sample Code

```psj {2}
Geometry.Part.Cube()
adjacent_elements = Geometry.ShowAdjacent.Elements(dAngle=5.0, crlStartElems=[Elem(1005)])
JPT.Debugger(adjacent_elements)
```
