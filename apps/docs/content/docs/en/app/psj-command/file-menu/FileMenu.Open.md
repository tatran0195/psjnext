---
title: "FileMenu.Open()"
description: "Load JTDB file"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "FileMenu > Open"
---

## Description

Load JTDB file

## Syntax

```psj
FileMenu.Open(strFileName="", bUseTmpTable=False)
```

## Inputs

### `strFileName` @type(String) @default("")

- The file name.

### `bUseTmpTable` @type(Boolean) @default(False)

- The use temporary table.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
FileMenu.Open(strFileName="", bUseTmpTable=False)
```
