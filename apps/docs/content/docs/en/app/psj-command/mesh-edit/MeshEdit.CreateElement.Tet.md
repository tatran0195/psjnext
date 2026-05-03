---
title: "MeshEdit.CreateElement.Tet()"
description: "create element Tet"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > CreateElement > Tet"
---

## Description

Create element Tet

## Syntax

```psj
MeshEdit.CreateElement.Tet(iParentEntityId=0, crlNodes=[], crlElems=[])
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
MeshEdit.CreateElement.Tet(iParentEntityId=0, crlNodes=[], crlElems=[])
```
