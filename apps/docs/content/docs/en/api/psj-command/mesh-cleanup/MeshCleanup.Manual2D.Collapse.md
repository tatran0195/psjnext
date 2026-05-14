---
title: "MeshCleanup.Manual2D.Collapse()"
description: "Delete and combine 2D element"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshCleanup > Manual2D > Collapse"
---

## Description

Delete and combine 2D element.

## Syntax

```psj
MeshCleanup.Manual2D.Collapse(crNodeRef=None, crNodeEq=None)
```

## Inputs

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crNodeRef`

- The reference node.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crNodeEq`

- The equivalence node.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {2}
Geometry.Part.Cube(strName="Cube _2", iPartColor=7434735)
MeshCleanup.Manual2D.Collapse(crNodeRef=Node(95), crNodeEq=Node(96))
```
