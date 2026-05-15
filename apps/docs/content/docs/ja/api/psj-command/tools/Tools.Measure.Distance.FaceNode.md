---
title: "Tools.Measure.Distance.FaceNode()"
description: "Measure Distance By FaceNode"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > Measure > Distance > FaceNode"
---

## Description

Measure Distance By FaceNode

## Syntax

```psj
Tools.Measure.Distance.FaceNode(crlFaces, crlNodes, iPrecision=6)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlFaces

- Specify the face.

<!-- @since:5.0.1 @required -->
### crlNodes

- Specify the node.

<!-- @since:5.0.1 @optional -->
### iPrecision

- Specify the precision.
- The default value is 6.

## Return Code

A _Double_ specifying the distance between face - node.

## Sample Code

```psj {2}
Geometry.Part.Trapezoid()
dist=Tools.Measure.Distance.FaceNode(crlFaces=[Face(23)], crlNodes=[Node(306)],iPrecision=15)
print(dist)
```
