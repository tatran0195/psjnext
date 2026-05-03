---
title: "Properties.Material.ImportFromMLIB()"
description: "Import materials from a .mlib file into the library database."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Properties > Material > ImportFromMLIB"
macro_link: "ImportFromMLIB"
---

## Description

Import materials from a .mlib file into the library database.

## Syntax

```psj
Properties.Material.ImportFromMLIB(...)
```

## Inputs

### `strFileName` @type(String) @default("")

- Path of .mlib file.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
# Import .mlib file from a shared folder on a network machine
Properties.Material.ImportFromMLIB(strFileName=r"\\NetworkMachine\shared_folder\sample.mlib")
```
