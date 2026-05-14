---
title: "Tools.Measure.Area.Element()"
description: "Measure Area By Element"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > Measure > Area > Element"
---

## Description

Measure Area By Element

## Syntax

```psj
Tools.Measure.Area.Element(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlElems`

- The element.

<!-- @since:5.0.1 @type:Integer @optional @default:6 -->
### `iPrecision`

- The precision.

## Return Code

A _Double_ specifying the area value of an element or a total area value of elements.

## Sample Code

```psj {3,6}
Geometry.Part.Cube()

area=Tools.Measure.Area.Element(crlElems=[Elem(1025,1026)])
JPT.Debugger(area)

area=Tools.Measure.Area.Element(crlElems=[Elem(1025,1026)], iPrecision=15)
JPT.Debugger(area)
```
