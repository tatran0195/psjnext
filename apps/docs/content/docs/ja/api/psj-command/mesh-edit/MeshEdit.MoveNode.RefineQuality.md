---
title: "MeshEdit.MoveNode.RefineQuality()"
description: "MeshEdit RefineQuality"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > MoveNode > RefineQuality"
---

## Description

MeshEdit RefineQuality

## Syntax

```psj
MeshEdit.MoveNode.RefineQuality(iMetric=0, crlFaces=[], crlElems=[], crlNodes=[])
```

## Inputs

<!-- @since:5.0.1 @optional -->
### iMetric

- Specify the metric.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crlFaces

- Specify the face.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlElems

- Specify the element.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlNodes

- Specify the node.
- The default value is \[].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.RefineQuality(iMetric=0, crlFaces=[], crlElems=[], crlNodes=[])
```
