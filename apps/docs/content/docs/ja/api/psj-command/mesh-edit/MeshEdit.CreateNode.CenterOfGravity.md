---
title: "MeshEdit.CreateNode.CenterOfGravity()"
description: "create node Center Of Gravity"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > CreateNode > CenterOfGravity"
---

## Description

Create node Center Of Gravity

## Syntax

```psj
MeshEdit.CreateNode.CenterOfGravity(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### iCreationType

- Specify the creation type.
  - 0: Gravity
  - 1: Shape
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### iNewNodeID

- Specify the new node ID.
- The default value is the maximum node ID + 1.

<!-- @since:5.0.1 @optional -->
### crlParts

- Specify the selected part.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlBarPart

- Specify the selected bar part.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlFaces

- Specify the selected face.
- The default value is \[].

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### iNodeID

- Specify the node ID.
- The default value is 0.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### dX

- Specify the x.
- The default value is 0.0.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### dY

- Specify the y.
- The default value is 0.0.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### dZ

- Specify the z.
- The default value is 0.0.

## Return Code

- A _Cursor_ specifying the created floating node.

## Sample Code

```psj {5}
# Prepare model
Geometry.Part.Cube()

# Create center node of gravity
newNode = MeshEdit.CreateNode.CenterOfGravity(iNodeID=489, crlTargets=[Part(1)])
JPT.Debugger(newNode) # for checking the return value
```
