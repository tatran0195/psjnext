---
title: "MeshCleanup.Manual2D.SplitElement.QuadTo2Quads()"
description: "Convert a single quadrilateral element into two quadrilateral elements."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshCleanup > Manual2D > SplitElement > QuadTo2Quads"
---

## Description

Convert a single quadrilateral element into two quadrilateral elements.

## Syntax

```psj
MeshCleanup.Manual2D.SplitElement.QuadTo2Quads(crlElems=[], crDatumNode0=None, crDatumNode1=None, iMethod=0, iAutoExecute=0, iAutoTransition=0, iCADProject=0, iMergeNode=0)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlElems`

- The element.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crDatumNode0`

- The datum node0.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crDatumNode1`

- The datum node1.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMethod`

- The method.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAutoExecute`

- The auto execute.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAutoTransition`

- The auto transition.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iCADProject`

- The CAD project.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMergeNode`

- The merge node.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual2D.SplitElement.QuadTo2Quads(crlElems=[], crDatumNode0=None, crDatumNode1=None, iMethod=0, iAutoExecute=0, iAutoTransition=0, iCADProject=0, iMergeNode=0)
```
