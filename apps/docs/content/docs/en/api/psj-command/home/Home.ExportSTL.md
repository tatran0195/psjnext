---
title: "Home.ExportSTL()"
description: "export stl"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Home > ExportSTL"
---

## Description

Export stl

## Syntax

```psj
Home.ExportSTL(strFile="", crlParts=[], dScale=1, bBinaryFormat=False)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strFile`

- The file.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlParts`

- The part.

<!-- @since:5.0.1 @type:Double @optional @default:1 -->
### `dScale`

- The scale.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bBinaryFormat`

- The filter index.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Home.ExportSTL(strFile="", crlParts=[], dScale=1, bBinaryFormat=False)
```
