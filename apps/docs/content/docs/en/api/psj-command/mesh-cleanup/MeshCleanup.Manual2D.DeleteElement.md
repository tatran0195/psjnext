---
title: "MeshCleanup.Manual2D.DeleteElement()"
description: "Delete Element"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshCleanup > Manual2D > DeleteElement"
---

## Description

Delete Element

## Syntax

```psj
MeshCleanup.Manual2D.DeleteElement(crlElems, bKeepShareElem=False)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlElems`

- The element.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bKeepShareElem`

- The keep share element.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual2D.DeleteElement(crlElems, bKeepShareElem=False)
```
