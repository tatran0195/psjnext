---
title: "MidPlaneEdit.Face.EdgesToEdges()"
description: "add face by edges"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MidPlaneEdit > Face > EdgesToEdges"
---

## Description

Add face by edges

## Syntax

```psj
MidPlaneEdit.Face.EdgesToEdges(crlEdges, bImprint=False, bMultiEdges=False)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlEdges

- Specify the edge.

<!-- @since:5.0.1 @optional -->
### bImprint

- Specify the imprint.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### bMultiEdges

- Specify the multi edges.
- The default value is False.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlaneEdit.Face.EdgesToEdges(crlEdges, bImprint=False, bMultiEdges=False)
```
