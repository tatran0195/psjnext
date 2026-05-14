---
title: "Geometry.Bar.Spline()"
description: "Create a spline-curve bar part passing though the selected nodes"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Bar > Spline"
---

## Description

Create a spline-curve bar part passing though the selected nodes.

## Syntax

```psj
Geometry.Bar.Spline(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlNodes`

- The either a series of nodes (interpolation points) through which the curve passes. At least three nodes must be specified.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crPart`

- The part that the spline bar will belong to. If set none, a new bar part will be created.

<!-- @since:5.0.1 @type:String @optional @default:"Bar _1" -->
### `strName`

- The name of new bar part.

## Return Code

A _Cursor_ specifying the created entity.
\- If _crPart_ = _None_ then return a cursor of new created bar part.
\- If _crPart_ is specified then return a cursor of new created edge.

## Sample Code

```psj {3}
Geometry.Part.Cube()

newBar = Geometry.Bar.Spline(crlNodes=[Node(440, 463, 443, 474)])
JPT.Debugger(newBar)
```
