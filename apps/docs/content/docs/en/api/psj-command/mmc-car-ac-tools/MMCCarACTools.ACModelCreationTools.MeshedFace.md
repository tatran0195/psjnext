---
title: "MMCCarACTools.ACModelCreationTools.MeshedFace()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MMCCarACTools > ACModelCreationTools > MeshedFace"
---

## Description

## Syntax

```psj
MMCCarACTools.ACModelCreationTools.MeshedFace(crlItem1, crlItem2, crlItem3, crlParts, iType, dMeshSise, bMergeTol, dTol, bCreatePart)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlItem1`

- The item1.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlItem2`

- The item2.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlItem3`

- The item3.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlParts`

- The part.

<!-- @since:5.0.1 @type:Integer @required -->
### `iType`

- The type.

<!-- @since:5.0.1 @type:Double @required -->
### `dMeshSise`

- The mesh sise.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bMergeTol`

- The merge tolerance.

<!-- @since:5.0.1 @type:Double @required -->
### `dTol`

- The tolerance.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bCreatePart`

- The create part.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MMCCarACTools.ACModelCreationTools.MeshedFace(crlItem1, crlItem2, crlItem3, crlParts, iType, dMeshSise, bMergeTol, dTol, bCreatePart)
```
