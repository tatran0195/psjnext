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

<!-- @since:5.0.1 @optional -->
### crlElems

- Specify the element.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iPrecision

- Specify the precision.
- The default value is 6.

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
