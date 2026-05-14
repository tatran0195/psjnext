---
title: "Geometry.Bar.Arc()"
description: "Create an arc-shaped bar part passing though the 3 selected nodes"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Bar > Arc (3 Nodes)"
---

## Description

Create an arc-shaped bar part passing though the 3 selected nodes.

## Syntax

```psj
Geometry.Bar.Arc(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlNodes`

- The three specified nodes to create arc.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crPart`

- The part that the arc-shaped bar will belong to. If set none, a new bar part will be created.

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

newBar = Geometry.Bar.Arc(crlNodes=[Node(446, 451, 474)])
JPT.Debugger(newBar)
```
