---
title: "MeshCleanup.Element.SolidElement()"
description: "Change Topology for Solid Element"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshCleanup > Element > SolidElement"
---

## Description

Change Topology for Solid Element

## Syntax

```psj
MeshCleanup.Element.SolidElement(crlElems, crPart=None)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlElems`

- The element.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crPart`

- The part.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Element.SolidElement(crlElems, crPart=None)
```
