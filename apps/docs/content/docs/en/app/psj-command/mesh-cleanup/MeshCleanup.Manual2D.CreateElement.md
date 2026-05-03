---
title: "MeshCleanup.Manual2D.CreateElement()"
description: "Create a Tri/Quad element"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshCleanup > Manual2D > CreateElement"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Create element","Create a Tri/Quad element"]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create a Tri/Quad element.

## Syntax

```psj
MeshCleanup.Manual2D.CreateElement()
```

## Inputs

### `iElemType` @type(Integer) @default(0)

- The element type.
  - 0: Tri element
  - 1: Quad element

### `crParentEntity` @type(Cursor) @default(None)

- The face to which the created element will belong.

### `crlNodes` @type(List\[Cursor]) @default(\[])

- The node.

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
