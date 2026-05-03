---
title: "MeshCleanup.Manual3D.CreateHex()"
description: "create hex8 elements"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshCleanup > Manual3D > CreateHex"
---

## Description

Create hex8 elements

## Syntax

```psj
MeshCleanup.Manual3D.CreateHex(iParentEntityId=0, crlElems=[], iSeprateN=1)
```

## Inputs

### `iParentEntityId` @type(Integer) @default(0)

- The parent entity ID.

### `crlElems` @type(List\[Cursor]) @default(\[])

- The element.

### `iSeprateN` @type(Integer) @default(1)

- The seprate n.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual3D.CreateHex(iParentEntityId=0, crlElems=[], iSeprateN=1)
```
