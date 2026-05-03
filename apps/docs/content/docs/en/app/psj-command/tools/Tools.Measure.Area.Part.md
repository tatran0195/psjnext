---
title: "Tools.Measure.Area.Part()"
description: "Measure Distance By FaceNode"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > Measure > Area > Part"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Measure Distance By FaceNode

## Syntax

```psj
Tools.Measure.Area.Part(crlParts=[], iPrecision=6)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @default(\[])

- The part.

### `iPrecision` @type(Integer) @default(6)

- The precision.

## Return Code

A _Double_ specifying the area value of a part or a total area value of parts.

## Sample Code

```psj
Tools.Measure.Area.Part(crlParts=[], iPrecision=6)
```
