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

<!-- @since:5.0.1 @required -->
### crlElems

- Specify the element.

<!-- @since:5.0.1 @optional -->
### crPart

- Specify the part.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Element.SolidElement(crlElems, crPart=None)
```
