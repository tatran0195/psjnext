---
title: "MeshCleanup.Manual2D.SplitElement.TriTo4Tris()"
description: "Convert a single triangle element into four triangular elements."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "MeshCleanup > Manual2D > SplitElement > TriTo4Tris"
---

## Description

Convert a single triangle element into four triangular elements.

## Syntax

```psj
MeshCleanup.Manual2D.SplitElement.TriTo4Tris(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlElems`

- The element.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crDatumNode0`

- The datum node0.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crDatumNode1`

- The datum node1.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iMethod`

- The method.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iAutoExecute`

- The auto execute.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iAutoTransition`

- The auto transition.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iCADProject`

- The CAD project.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iMergeNode`

- The merge node.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {4}
# Prepare model
Geometry.Part.Cube(ilAxialNodes=[3, 3, 3], iPartColor=7463537)

# Devide Triangle Element 76 into 4 smaller trianbles.
MeshCleanup.Manual2D.SplitElement.TriTo4Tris(crlElems=[Elem(76)], iMethod=8, iAutoExecute=1, iMergeNode=1)
```
