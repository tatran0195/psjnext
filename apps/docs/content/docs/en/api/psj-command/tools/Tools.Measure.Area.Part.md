---
title: "Tools.Measure.Area.Part()"
description: "Measure Distance By FaceNode"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > Measure > Area > Part"
---

## Description

Measure Distance By FaceNode

## Syntax

```psj
Tools.Measure.Area.Part(crlParts=[], iPrecision=6)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlParts`

- The part.

<!-- @since:5.0.1 @type:Integer @optional @default:6 -->
### `iPrecision`

- The precision.

## Return Code

A _Double_ specifying the area value of a part or a total area value of parts.

## Sample Code

```psj
Tools.Measure.Area.Part(crlParts=[], iPrecision=6)
```
