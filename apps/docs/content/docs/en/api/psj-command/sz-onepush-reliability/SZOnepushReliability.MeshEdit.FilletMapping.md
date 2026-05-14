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

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlParts`

- The part.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlFaces`

- The face.

<!-- @since:5.0.1 @type:Double @required -->
### `dMinRadius`

- The minimum radius.

<!-- @since:5.0.1 @type:Double @required -->
### `dMaxRadius`

- The maximum radius.

<!-- @since:5.0.1 @type:Double @required -->
### `dMinAngle`

- The minimum angle.

<!-- @since:5.0.1 @type:Double @required -->
### `dMaxAngle`

- The maximum angle.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bConvex`

- The convex.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bConcave`

- The concave.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
SZOnepushReliability.MeshEdit.FilletMapping(crlParts, crlFaces, dMinRadius, dMaxRadius, dMinAngle, dMaxAngle, bConvex, bConcave)
```
