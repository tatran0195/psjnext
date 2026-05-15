---
title: "SZOnepushReliability.MeshEdit.FilletMapping()"
description: "Fillet mapping"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "SZOnepushReliability > MeshEdit > FilletMapping"
---

## Description

Fillet mapping

## Syntax

```psj
SZOnepushReliability.MeshEdit.FilletMapping(crlParts, crlFaces, dMinRadius, dMaxRadius, dMinAngle, dMaxAngle, bConvex, bConcave)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlParts

- Specify the part.

<!-- @since:5.0.1 @required -->
### crlFaces

- Specify the face.

<!-- @since:5.0.1 @required -->
### dMinRadius

- Specify the minimum radius.

<!-- @since:5.0.1 @required -->
### dMaxRadius

- Specify the maximum radius.

<!-- @since:5.0.1 @required -->
### dMinAngle

- Specify the minimum angle.

<!-- @since:5.0.1 @required -->
### dMaxAngle

- Specify the maximum angle.

<!-- @since:5.0.1 @required -->
### bConvex

- Specify the convex.

<!-- @since:5.0.1 @required -->
### bConcave

- Specify the concave.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
SZOnepushReliability.MeshEdit.FilletMapping(crlParts, crlFaces, dMinRadius, dMaxRadius, dMinAngle, dMaxAngle, bConvex, bConcave)
```
