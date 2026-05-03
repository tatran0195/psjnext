---
title: "ExManifoldModeling.SZ.WeldLine2()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "ExManifoldModeling > SZ > WeldLine2"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description is missing in all versions — placeholder inserted
-->

## Description

## Syntax

```psj
ExManifoldModeling.SZ.WeldLine2(crlFaces, crlParts, dLayerWidth, iLayerNumber)
```

## Inputs

### `crlFaces` @type(List\[Cursor]) @required

- The face.

### `crlParts` @type(List\[Cursor]) @required

- The part.

### `dLayerWidth` @type(Double) @required

- The layer width.

### `iLayerNumber` @type(Integer) @required

- The layer number.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
ExManifoldModeling.SZ.WeldLine2(crlFaces, crlParts, dLayerWidth, iLayerNumber)
```
