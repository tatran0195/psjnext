---
title: "MeshEdit.CreateElement.Hex()"
description: "create hex8 elements"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > CreateElement > Hex"
---

## Description

Create hex8 elements

## Syntax

```psj
MeshEdit.CreateElement.Hex(iParentEntityId=0, crlElems=[], iSeprateN=1)
```

## Inputs

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iParentEntityId`

- The parent entity ID.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlElems`

- The element.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iSeprateN`

- The seprate n.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.CreateElement.Hex(iParentEntityId=0, crlElems=[], iSeprateN=1)
```
