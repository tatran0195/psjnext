---
title: "Test.Muffler.ProjectLineForWeld()"
description: "Projec line for weld"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Test > Muffler > ProjectLineForWeld"
---

## Description

Projec line for weld

## Syntax

```psj
Test.Muffler.ProjectLineForWeld(crlEdges, crlFaces)
```

## Inputs

### `crlEdges` @type(List\[Cursor]) @required

- The edge.

### `crlFaces` @type(List\[Cursor]) @required

- The face.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Test.Muffler.ProjectLineForWeld(crlEdges, crlFaces)
```
