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

<!-- @since:5.1.0 @optional -->
### crlElems

- Specify the element.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### crDatumNode0

- Specify the datum node0.
- The default value is None.

<!-- @since:5.1.0 @optional -->
### crDatumNode1

- Specify the datum node1.
- The default value is None.

<!-- @since:5.1.0 @optional -->
### iMethod

- Specify the method.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iAutoExecute

- Specify the auto execute.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iAutoTransition

- Specify the auto transition.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iCADProject

- Specify the CAD project.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iMergeNode

- Specify the merge node.
- The default value is 0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```pj {4}
# Prepare model
Geometry.Part.Cube(ilAxialNodes=[3, 3, 3], iPartColor=7463537)

# Devide Triangle Element 76 into 4 smaller trianbles.
MeshCleanup.Manual2D.SplitElement.TriTo4Tris(crlElems=[Elem(76)], iMethod=8, iAutoExecute=1, iMergeNode=1)
```
