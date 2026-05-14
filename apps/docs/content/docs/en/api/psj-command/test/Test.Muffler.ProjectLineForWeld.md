---
title: "Test.Muffler.ProjectLineForWeld()"
description: "Projec line for weld"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Test > Muffler > ProjectLineForWeld"
---

## Description

Projec line for weld

## Syntax

```psj
Test.Muffler.ProjectLineForWeld(crlEdges, crlFaces)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlEdges`

- The edge.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlFaces`

- The face.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Test.Muffler.ProjectLineForWeld(crlEdges, crlFaces)
```
