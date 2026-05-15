---
title: "MeshEdit.CreateElement.Quad4()"
description: "Create element"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > CreateElement > Quad4"
---

## Description

Create element

## Syntax

```psj
MeshEdit.CreateElement.Quad4(iElemType=0, crParentEntity=None, crlNodes=[])
```

## Inputs

<!-- @since:5.0.1 @optional -->
### iElemType

- Specify the element type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crParentEntity

- Specify the parent entity.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crlNodes

- Specify the node.
- The default value is \[].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.CreateElement.Quad4(iElemType=0, crParentEntity=None, crlNodes=[])
```
