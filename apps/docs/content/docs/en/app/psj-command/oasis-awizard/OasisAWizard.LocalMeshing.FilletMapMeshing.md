---
title: "OasisAWizard.LocalMeshing.FilletMapMeshing()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "OasisAWizard > LocalMeshing > FilletMapMeshing"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description is missing in all versions — placeholder inserted
-->

## Description

## Syntax

```psj
OasisAWizard.LocalMeshing.FilletMapMeshing(crlParts=[], crlFaces=[], dMinLength=0.0, dMaxLength=1.0, dMinRadius=0.0, dMaxRadius=9e-3, bConvex=True, bConcave=True, iTmp=0, dLengthSingleLayer=0, dBMinLengthForSingleLayer=0, dRadiusSingleLayer=0, dBMinRadiusForSingleLayer=0, iMinlayer=0, bMinLayer=False)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @default(\[])

- The part.

### `crlFaces` @type(List\[Cursor]) @default(\[])

- The face.

### `dMinLength` @type(Double) @default(0.0)

- The minimum length.

### `dMaxLength` @type(Double) @default(1.0)

- The maximum length.

### `dMinRadius` @type(Double) @default(0.0)

- The minimum radius.

### `dMaxRadius` @type(Double) @default(9e-3)

- The maximum radius.

### `bConvex` @type(Boolean) @default(True)

- The convex.

### `bConcave` @type(Boolean) @default(True)

- The concave.

### `iTmp` @type(Integer) @default(0)

- The temporary.

### `dLengthSingleLayer` @type(Double) @default(0)

- The length single layer.

### `dBMinLengthForSingleLayer` @type(Double) @default(0)

- The minimum length for single layer.

### `dRadiusSingleLayer` @type(Double) @default(0)

- The radius single layer.

### `dBMinRadiusForSingleLayer` @type(Double) @default(0)

- The minimum radius for single layer.

### `iMinlayer` @type(Integer) @default(0)

- The minlayer.

### `bMinLayer` @type(Boolean) @default(False)

- The minimum layer.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
OasisAWizard.LocalMeshing.FilletMapMeshing(crlParts=[], crlFaces=[], dMinLength=0.0, dMaxLength=1.0, dMinRadius=0.0, dMaxRadius=9e-3, bConvex=True, bConcave=True, iTmp=0, dLengthSingleLayer=0, dBMinLengthForSingleLayer=0, dRadiusSingleLayer=0, dBMinRadiusForSingleLayer=0, iMinlayer=0, bMinLayer=False)
```
