---
title: "MeshCleanup.Manual2D.SplitElement.TriTo4Tris()"
description: "Convert a single triangle element into four triangular elements."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "MeshCleanup > Manual2D > SplitElement > TriTo4Tris"
---

## Description

Convert a single triangle element into four triangular elements.

## Syntax

```psj
MeshCleanup.Manual2D.SplitElement.TriTo4Tris(...)
```

## Inputs

### `crlElems` @type(List\[Cursor]) @default(\[])

- The element.

### `crDatumNode0` @type(Cursor) @default(None)

- The datum node0.

### `crDatumNode1` @type(Cursor) @default(None)

- The datum node1.

### `iMethod` @type(Integer) @default(0)

- The method.

### `iAutoExecute` @type(Integer) @default(0)

- The auto execute.

### `iAutoTransition` @type(Integer) @default(0)

- The auto transition.

### `iCADProject` @type(Integer) @default(0)

- The CAD project.

### `iMergeNode` @type(Integer) @default(0)

- The merge node.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj{4}
# Prepare model
Geometry.Part.Cube(ilAxialNodes=[3, 3, 3], iPartColor=7463537)

# Devide Triangle Element 76 into 4 smaller trianbles.
MeshCleanup.Manual2D.SplitElement.TriTo4Tris(crlElems=[Elem(76)], iMethod=8, iAutoExecute=1, iMergeNode=1)
```
