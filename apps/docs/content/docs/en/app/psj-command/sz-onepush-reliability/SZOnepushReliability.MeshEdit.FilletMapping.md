---
title: "SZOnepushReliability.MeshEdit.FilletMapping()"
description: "Fillet mapping"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "SZOnepushReliability > MeshEdit > FilletMapping"
---

## Description

Fillet mapping

## Syntax

```psj
SZOnepushReliability.MeshEdit.FilletMapping(crlParts, crlFaces, dMinRadius, dMaxRadius, dMinAngle, dMaxAngle, bConvex, bConcave)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @required

- The part.

### `crlFaces` @type(List\[Cursor]) @required

- The face.

### `dMinRadius` @type(Double) @required

- The minimum radius.

### `dMaxRadius` @type(Double) @required

- The maximum radius.

### `dMinAngle` @type(Double) @required

- The minimum angle.

### `dMaxAngle` @type(Double) @required

- The maximum angle.

### `bConvex` @type(Boolean) @required

- The convex.

### `bConcave` @type(Boolean) @required

- The concave.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
SZOnepushReliability.MeshEdit.FilletMapping(crlParts, crlFaces, dMinRadius, dMaxRadius, dMinAngle, dMaxAngle, bConvex, bConcave)
```
