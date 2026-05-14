---
title: "NSModeling.NSModeling _Close _Hole()"
description: "NSModeling NSModeling _Close _Hole"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "NSModeling > NSModeling _Close _Hole"
---

## Description

NSModeling NSModeling\_Close\_Hole

## Syntax

```psj
NSModeling.NSModeling _Close _Hole(iType, dMaxLength, bMergeFaces, bSetCenterPoint, crlNodes, crlParts)
```

## Inputs

<!-- @since:5.0.1 @type:Integer @required -->
### `iType`

- The type.

<!-- @since:5.0.1 @type:Double @required -->
### `dMaxLength`

- The maximum length.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bMergeFaces`

- The merge faces.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bSetCenterPoint`

- The set center point.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlNodes`

- The node.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlParts`

- The part.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
NSModeling.NSModeling _Close _Hole(iType, dMaxLength, bMergeFaces, bSetCenterPoint, crlNodes, crlParts)
```
