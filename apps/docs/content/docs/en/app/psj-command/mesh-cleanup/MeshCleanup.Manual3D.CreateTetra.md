---
title: "MeshCleanup.Manual3D.CreateTetra()"
description: "create element Tet"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshCleanup > Manual3D > CreateTetra"
---

## Description

Create element Tet

## Syntax

```psj
MeshCleanup.Manual3D.CreateTetra(iParentEntityId=0, crlNodes=[], crlElems=[])
```

## Inputs

### `iParentEntityId` @type(Integer) @default(0)

- The parent entity ID.

### `crlNodes` @type(List\[Cursor]) @default(\[])

- The node.

### `crlElems` @type(List\[Cursor]) @default(\[])

- The element.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual3D.CreateTetra(iParentEntityId=0, crlNodes=[], crlElems=[])
```
