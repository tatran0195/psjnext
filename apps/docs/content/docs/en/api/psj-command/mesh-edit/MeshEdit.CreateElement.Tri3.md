---
title: "MeshEdit.CreateElement.Tri3()"
description: "Create element"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > CreateElement > Tri3"
---

## Description

Create element

## Syntax

```psj
MeshEdit.CreateElement.Tri3(iElemType=0, crParentEntity=None, crlNodes=[])
```

## Inputs

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iElemType`

- The element type.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crParentEntity`

- The parent entity.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlNodes`

- The node.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.CreateElement.Tri3(iElemType=0, crParentEntity=None, crlNodes=[])
```
