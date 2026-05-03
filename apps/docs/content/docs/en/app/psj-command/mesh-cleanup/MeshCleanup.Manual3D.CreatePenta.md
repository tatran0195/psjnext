---
title: "MeshCleanup.Manual3D.CreatePenta()"
description: "Create penta5 element"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshCleanup > Manual3D > CreatePenta"
---

## Description

Create penta5 element

## Syntax

```psj
MeshCleanup.Manual3D.CreatePenta(iParentEntityId=0, crlElems=[])
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
MeshCleanup.Manual3D.CreatePenta(iParentEntityId=0, crlElems=[])
```
