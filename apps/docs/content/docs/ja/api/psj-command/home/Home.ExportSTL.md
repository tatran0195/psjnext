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

<!-- @since:5.0.1 @optional -->
### strFile

- Specify the file.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### crlParts

- Specify the part.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dScale

- Specify the scale.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### bBinaryFormat

- Specify the filter index.
- The default value is False.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Home.ExportSTL(strFile="", crlParts=[], dScale=1, bBinaryFormat=False)
```
