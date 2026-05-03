---
title: "MeshCleanup.Element.SolidElement()"
description: "Change Topology for Solid Element"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshCleanup > Element > SolidElement"
---

## Description

Change Topology for Solid Element

## Syntax

```psj
MeshCleanup.Element.SolidElement(crlElems, crPart=None)
```

## Inputs

### `crlElems` @type(List\[Cursor]) @required

- The element.

### `crPart` @type(Cursor) @default(None)

- The part.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Element.SolidElement(crlElems, crPart=None)
```
