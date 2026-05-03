---
title: "Tools.Measure.Area.Element()"
description: "Measure Area By Element"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > Measure > Area > Element"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Measure Distance By FaceNode","Measure Area By Element"]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Measure Area By Element

## Syntax

```psj
Tools.Measure.Area.Element(...)
```

## Inputs

### `crlElems` @type(List\[Cursor]) @default(\[])

- The element.

### `iPrecision` @type(Integer) @default(6)

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
