---
title: "MeshCleanup.ChangeTopology.Element.SurfaceElement()"
description: "Assign the selected element to a different part."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshCleanup > ChangeTopology > Element > SurfaceElement"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Unknown Description","Assign the selected element to a different part."]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Assign the selected element to a different part.

## Syntax

```psj
MeshCleanup.ChangeTopology.Element.SurfaceElement(ilElement, ilFace, ilPart, iCreateNewPart)
```

## Inputs

### `ilElement` @type(List\[Integer]) @required

- The element.

### `ilFace` @type(List\[Integer]) @required

- The face.

### `ilPart` @type(List\[Integer]) @required

- The part.

### `iCreateNewPart` @type(Integer) @required

- The create new part.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.ChangeTopology.Element.SurfaceElement(ilElement, ilFace, ilPart, iCreateNewPart)
```
