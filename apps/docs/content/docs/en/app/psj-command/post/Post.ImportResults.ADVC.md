---
title: "Post.ImportResults.ADVC()"
description: "Unknown Description"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Post > ImportResults > ADVC"
---

## Description

Unknown Description

## Syntax

```psj
Post.ImportResults.ADVC(strlPath=[], iImportType=1, dFaceAngle=60.0, dEdgeAngle=60.0)
```

## Inputs

### `strlPath` @type(List\[String]) @default(\[])

- The path.

### `iImportType` @type(Integer) @default(1)

- The import type.

### `dFaceAngle` @type(Double) @default(60.0)

- The face angle.

### `dEdgeAngle` @type(Double) @default(60.0)

- The edge angle.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Post.ImportResults.ADVC(strlPath=[], iImportType=1, dFaceAngle=60.0, dEdgeAngle=60.0)
```
