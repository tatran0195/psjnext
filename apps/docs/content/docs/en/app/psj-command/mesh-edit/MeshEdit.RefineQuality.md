---
title: "MeshEdit.RefineQuality()"
description: "Resolve poor-quality mesh within the selected face/element/node set by relocating mesh nodes."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > RefineQuality"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Unknown Description","Resolve poor-quality mesh within the selected face/element/node set by relocating mesh nodes."]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Resolve poor-quality mesh within the selected face/element/node set by relocating mesh nodes.

## Syntax

```psj
MeshEdit.RefineQuality(iMetric, crlFaces, crlElems, crlNodes)
```

## Inputs

### `iMetric` @type(Integer) @required

- The metric.

### `crlFaces` @type(List\[Cursor]) @required

- The face.

### `crlElems` @type(List\[Cursor]) @required

- The element.

### `crlNodes` @type(List\[Cursor]) @required

- The node.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.RefineQuality(iMetric, crlFaces, crlElems, crlNodes)
```
