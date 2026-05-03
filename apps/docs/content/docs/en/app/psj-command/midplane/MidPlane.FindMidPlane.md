---
title: "MidPlane.FindMidPlane()"
description: "Create mid-planes for the specified parts."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MidPlane > FindMidPlane"
macro_link: "FindMidPlane"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Unknown Description","Create mid-planes for the specified parts."]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create mid-planes for the specified parts.

## Syntax

```psj
MidPlane.FindMidPlane(...)
```

## Inputs

### `crlTargetParts` @type(List\[Cursor]) @default(\[]) @since(5.1.0)

- Parts.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {6}
Geometry.Part.Cube(dlLength=[0.001, 0.01, 0.01])
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0],
                    dlLength=[0.002, 0.01, 0.01],
                    strName="Cube_2",
                    iPartColor=6409934)
MidPlane.FindMidPlane(crlTargetParts=[Part(1, 2)])
```
