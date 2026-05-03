---
title: "MeshCleanup.Manual2D.DeleteElement()"
description: "Delete Element"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshCleanup > Manual2D > DeleteElement"
---

## Description

Delete Element

## Syntax

```psj
MeshCleanup.Manual2D.DeleteElement(crlElems, bKeepShareElem=False)
```

## Inputs

### `crlElems` @type(List\[Cursor]) @required

- The element.

### `bKeepShareElem` @type(Boolean) @default(False)

- The keep share element.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual2D.DeleteElement(crlElems, bKeepShareElem=False)
```
