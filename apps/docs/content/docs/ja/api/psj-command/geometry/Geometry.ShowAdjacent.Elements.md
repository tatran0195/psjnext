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

<!-- @since:5.0.1 @optional -->
### dAngle

- Specify the angle between elements in degree. The adjacent elements that are at an angle of less than or equal to _dAngle_ will be selected.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### bIncludeStopElems

- Specify whether to add the stop elements to the selection list or not.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### iNumOfLayers

- Specify the number of adjacent layers to be searched.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### crlStartElems

- Specify a sequence of the start elements.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlStopElems

- Specify a sequence of the stop elements.
- The default value is \[].

## Return Code

A _List of Cursor_ specifying a sequence of adjacent elements.

## Sample Code

```psj {2}
Geometry.Part.Cube()
adjacent _elements = Geometry.ShowAdjacent.Elements(dAngle=5.0, crlStartElems=[Elem(1005)])
JPT.Debugger(adjacent _elements)
```
