---
title: "MeshCleanup.Manual3D.CreateTetra()"
description: "create element Tet"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshCleanup > Manual3D > CreateTetra"
---

## Description

Create element Tet

## Syntax

```psj
MeshCleanup.Manual3D.CreateTetra(iParentEntityId=0, crlNodes=[], crlElems=[])
```

## Inputs

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iParentEntityId`

- The parent entity ID.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlNodes`

- The node.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlElems`

- The element.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual3D.CreateTetra(iParentEntityId=0, crlNodes=[], crlElems=[])
```
