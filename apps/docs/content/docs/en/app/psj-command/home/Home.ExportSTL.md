---
title: "Home.ExportSTL()"
description: "export stl"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Home > ExportSTL"
---

## Description

Export stl

## Syntax

```psj
Home.ExportSTL(strFile="", crlParts=[], dScale=1, bBinaryFormat=False)
```

## Inputs

### `strFile` @type(String) @default("")

- The file.

### `crlParts` @type(List\[Cursor]) @default(\[])

- The part.

### `dScale` @type(Double) @default(1)

- The scale.

### `bBinaryFormat` @type(Boolean) @default(False)

- The filter index.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Home.ExportSTL(strFile="", crlParts=[], dScale=1, bBinaryFormat=False)
```
