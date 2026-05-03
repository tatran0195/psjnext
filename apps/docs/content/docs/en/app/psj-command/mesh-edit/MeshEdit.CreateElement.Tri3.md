---
title: "MeshEdit.CreateElement.Tri3()"
description: "Create element"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > CreateElement > Tri3"
---

## Description

Create element

## Syntax

```psj
MeshEdit.CreateElement.Tri3(iElemType=0, crParentEntity=None, crlNodes=[])
```

## Inputs

### `iElemType` @type(Integer) @default(0)

- The element type.

### `crParentEntity` @type(Cursor) @default(None)

- The parent entity.

### `crlNodes` @type(List\[Cursor]) @default(\[])

- The node.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.CreateElement.Tri3(iElemType=0, crParentEntity=None, crlNodes=[])
```
