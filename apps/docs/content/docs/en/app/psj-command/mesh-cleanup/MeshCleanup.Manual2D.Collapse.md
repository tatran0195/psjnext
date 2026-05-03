---
title: "MeshCleanup.Manual2D.Collapse()"
description: "Delete and combine 2D element"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshCleanup > Manual2D > Collapse"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Collapse for Mesh Cleanup","Delete and combine 2D element"]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Delete and combine 2D element.

## Syntax

```psj
MeshCleanup.Manual2D.Collapse(crNodeRef=None, crNodeEq=None)
```

## Inputs

### `crNodeRef` @type(Cursor) @default(None)

- The reference node.

### `crNodeEq` @type(Cursor) @default(None)

- The equivalence node.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {2}
Geometry.Part.Cube(strName="Cube_2", iPartColor=7434735)
MeshCleanup.Manual2D.Collapse(crNodeRef=Node(95), crNodeEq=Node(96))
```
