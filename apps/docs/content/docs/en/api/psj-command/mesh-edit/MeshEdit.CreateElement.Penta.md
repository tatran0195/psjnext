---
title: "MeshEdit.CreateElement.Penta()"
description: "Create penta element"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > CreateElement > Penta"
---

## Description

Create penta element

## Syntax

```psj
MeshEdit.CreateElement.Penta(iParentEntityId=0, crlElems=[])
```

## Inputs

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iParentEntityId`

- The parent entity ID.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlElems`

- The element.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.CreateElement.Penta(iParentEntityId=0, crlElems=[])
```
