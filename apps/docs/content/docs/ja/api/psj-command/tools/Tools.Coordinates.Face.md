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

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "CRect1".

<!-- @since:5.0.1 @optional -->
### iCoordType

- Specify the coordinate type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iOrder

- Specify the order.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### veclPoint

- Specify the point.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlNodes

- Specify the node.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crItem

- Specify the item.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crRefCoord

- Specify the reference coordinate.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the edit.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.Coordinates.Face(strName="CRect1", iCoordType=0, iOrder=0, veclPoint=[], crlNodes=[], crItem=None, crRefCoord=None, crEdit=None)
```
