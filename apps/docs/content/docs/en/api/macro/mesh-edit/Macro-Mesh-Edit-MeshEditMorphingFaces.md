---
title: "MeshEditMorphingFaces()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Move nodes by effect range from a selected node.

## Syntax

```psj
MeshEditMorphingFaces(Cursor[] taFaceMove, Cursor[] taFaceFixed, bool DirectionType, Cursor Coordinate, Vector Offset, double Offset, int DistType, double DistStrong, double dDistWeak, int nodeID, Vector pointPosition )
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

A Cursor List specifying the node move.

<!-- @since:5.0.1 -->
### 2. Cursor\[]

A Cursor List specifying the face fixed.

<!-- @since:5.0.1 -->
### 3. Bool

A Bool specifying the Direction Type.

<!-- @since:5.0.1 -->
### 4. Cursor

A Cursor specifying the Coordinate.

<!-- @since:5.0.1 -->
### 5. Double\[]

A Double vector specifying the dist strong for Direction Type: Offset values.

<!-- @since:5.0.1 -->
### 6. Double

A Double specifying the move distance for Direction Type: Normal Offset.

<!-- @since:5.0.1 -->
### 7. Int

An Int specifying the Effect Range.

<!-- @since:5.0.1 -->
### 8. Double

A Double specifying the dist strong.

<!-- @since:5.0.1 -->
### 9. Double

A Double specifying the dist weak.

<!-- @since:5.0.1 -->
### 10. Int

An Int specifying the rotation center for Direction Type: Rotation.

<!-- @since:5.0.1 -->
### 11. Vector

A Double vector specifying the position of point for Direction Type: Node+Point.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MeshEditMorphingFaces([6:26], [], 0, 0:0, [0, 0.001, 0], 0, 0, 0.01, 0.02, -1, [])
```
