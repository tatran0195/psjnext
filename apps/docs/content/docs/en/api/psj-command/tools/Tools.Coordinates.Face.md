---
title: "Tools.Coordinates.Face()"
description: "create Coordinate by Face"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > Coordinates > Face"
---

## Description

Create Coordinate by Face

## Syntax

```psj
Tools.Coordinates.Face(strName="CRect1", iCoordType=0, iOrder=0, veclPoint=[], crlNodes=[], crItem=None, crRefCoord=None, crEdit=None)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"CRect1" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iCoordType`

- The coordinate type.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iOrder`

- The order.

<!-- @since:5.0.1 @type:Vector List @optional @default:[] -->
### `veclPoint`

- The point.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlNodes`

- The node.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crItem`

- The item.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crRefCoord`

- The reference coordinate.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.Coordinates.Face(strName="CRect1", iCoordType=0, iOrder=0, veclPoint=[], crlNodes=[], crItem=None, crRefCoord=None, crEdit=None)
```
