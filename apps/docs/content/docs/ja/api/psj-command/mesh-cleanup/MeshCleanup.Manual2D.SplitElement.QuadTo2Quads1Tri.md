---
title: "MeshCleanup.Manual2D.SplitElement.QuadTo2Quads1Tri()"
description: "Convert a single quadrilateral element into two quadrilateral elements and one triangular element."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshCleanup > Manual2D > SplitElement > QuadTo2Quads1Tri"
---

## Description

Convert a single quadrilateral element into two triangular elements.

## Syntax

```psj
MeshCleanup.Manual2D.SplitElement.QuadTo2Quads1Tri(crlElems=[], crDatumNode0=None, crDatumNode1=None, iMethod=0, iAutoExecute=0, iAutoTransition=0, iCADProject=0, iMergeNode=0)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlElems

- Specify the element.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crDatumNode0

- Specify the datum node0.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crDatumNode1

- Specify the datum node1.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the method.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iAutoExecute

- Specify the auto execute.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iAutoTransition

- Specify the auto transition.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iCADProject

- Specify the CAD project.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iMergeNode

- Specify the merge node.
- The default value is 0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual2D.SplitElement.QuadTo2Quads1Tri(crlElems=[], crDatumNode0=None, crDatumNode1=None, iMethod=0, iAutoExecute=0, iAutoTransition=0, iCADProject=0, iMergeNode=0)
```
