---
title: "MeshCleanup.Manual2D.CreateElement()"
description: "Create a Tri/Quad element"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshCleanup > Manual2D > CreateElement"
---

## Description

Create a Tri/Quad element.

## Syntax

```psj
MeshCleanup.Manual2D.CreateElement()
```

## Inputs

<!-- @since:5.0.1 @optional -->
### iElemType

- Specify the element type.
  - 0: Tri element
  - 1: Quad element
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crParentEntity

- Specify the face to which the created element will belong.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crlNodes

- Specify the node.
- The default value is \[].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {3-4}
Geometry.Part.Cube(iPartColor=6409934)
MeshCleanup.Manual2D.DeleteElement(crlElems=[Elem(1028)])
element = MeshCleanup.Manual2D.CreateElement(crParentEntity=Face(26), 
                                            crlNodes=[Node(470, 469, 461)])
JPT.Debugger(element)
```
