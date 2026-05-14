---
title: "Geometry.ShowAdjacent.Elements()"
description: "Expand the selection in all directions, regardless of the shape of surrounding features or the angle at which objects are joined. It obtained by recursively finding adjacent elements at an angle of less than or equal to the specified angle"
version _introduced: "5.0.1"
available _versions: "all"
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

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dAngle`

- The angle between elements in degree. The adjacent elements that are at an angle of less than or equal to _dAngle_ will be selected.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bIncludeStopElems`

- Whether to add the stop elements to the selection list or not.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iNumOfLayers`

- The number of adjacent layers to be searched.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlStartElems`

- A sequence of the start elements.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlStopElems`

- A sequence of the stop elements.

## Return Code

A _List of Cursor_ specifying a sequence of adjacent elements.

## Sample Code

```psj {2}
Geometry.Part.Cube()
adjacent _elements = Geometry.ShowAdjacent.Elements(dAngle=5.0, crlStartElems=[Elem(1005)])
JPT.Debugger(adjacent _elements)
```
