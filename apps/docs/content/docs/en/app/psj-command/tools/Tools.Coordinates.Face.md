---
title: "Tools.Coordinates.Face()"
description: "create Coordinate by Face"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > Coordinates > Face"
---

## Description

Create Coordinate by Face

## Syntax

```psj
Tools.Coordinates.Face(strName="CRect1", iCoordType=0, iOrder=0, veclPoint=[], crlNodes=[], crItem=None, crRefCoord=None, crEdit=None)
```

## Inputs

### `strName` @type(String) @default("CRect1")

- The name.

### `iCoordType` @type(Integer) @default(0)

- The coordinate type.

### `iOrder` @type(Integer) @default(0)

- The order.

### `veclPoint` @type(Vector List) @default(\[])

- The point.

### `crlNodes` @type(List\[Cursor]) @default(\[])

- The node.

### `crItem` @type(Cursor) @default(None)

- The item.

### `crRefCoord` @type(Cursor) @default(None)

- The reference coordinate.

### `crEdit` @type(Cursor) @default(None)

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.Coordinates.Face(strName="CRect1", iCoordType=0, iOrder=0, veclPoint=[], crlNodes=[], crItem=None, crRefCoord=None, crEdit=None)
```
