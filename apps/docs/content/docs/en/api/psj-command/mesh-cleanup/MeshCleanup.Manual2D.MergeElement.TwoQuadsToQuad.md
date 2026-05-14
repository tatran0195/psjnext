---
title: "MeshCleanup.Manual2D.MergeElement.TwoQuadsToQuad()"
description: "Merge two Quad elements into one Quad element"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshCleanup > Manual2D > MergeElement > TwoQuadsToQuad"
---

## Description

Merge two Quad elements into one Quad element

## Syntax

```psj
MeshCleanup.Manual2D.MergeElement.TwoQuadsToQuad(crlElems)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlElems`

- The element.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual2D.MergeElement.TwoQuadsToQuad(crlElems)
```
