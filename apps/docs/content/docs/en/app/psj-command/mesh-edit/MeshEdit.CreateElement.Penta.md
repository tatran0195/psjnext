---
title: "MeshEdit.CreateElement.Penta()"
description: "Create penta element"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > CreateElement > Penta"
---

## Description

Create penta element

## Syntax

```psj
MeshEdit.CreateElement.Penta(iParentEntityId=0, crlElems=[])
```

## Inputs

### `iParentEntityId` @type(Integer) @default(0)

- The parent entity ID.

### `crlElems` @type(List\[Cursor]) @default(\[])

- The element.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.CreateElement.Penta(iParentEntityId=0, crlElems=[])
```
