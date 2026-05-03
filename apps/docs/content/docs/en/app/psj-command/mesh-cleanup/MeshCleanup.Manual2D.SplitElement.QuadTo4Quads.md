---
title: "MeshCleanup.Manual2D.SplitElement.QuadTo4Quads()"
description: "Convert a single quadrilateral element into four quadrilateral elements."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshCleanup > Manual2D > SplitElement > QuadTo4Quads"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Split element 2D","Convert a single quadrilateral element into four quadrilateral elements."]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Convert a single quadrilateral element into four quadrilateral elements.

## Syntax

```psj
MeshCleanup.Manual2D.SplitElement.QuadTo4Quads(crlElems=[], crDatumNode0=None, crDatumNode1=None, iMethod=0, iAutoExecute=0, iAutoTransition=0, iCADProject=0, iMergeNode=0)
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

```psj
MeshCleanup.Manual2D.SplitElement.QuadTo4Quads(crlElems=[], crDatumNode0=None, crDatumNode1=None, iMethod=0, iAutoExecute=0, iAutoTransition=0, iCADProject=0, iMergeNode=0)
```
