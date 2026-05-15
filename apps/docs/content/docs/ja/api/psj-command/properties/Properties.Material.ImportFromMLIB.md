---
title: "Properties.Material.ImportFromMLIB()"
description: "Import materials from a .mlib file into the library database."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Properties > Material > ImportFromMLIB"
macro _link: "ImportFromMLIB"
---

## Description

Import materials from a .mlib file into the library database.

## Syntax

```psj
Properties.Material.ImportFromMLIB(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### strFileName

- Specify path of .mlib file.
- The default value is "".

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
# Import .mlib file from a shared folder on a network machine
Properties.Material.ImportFromMLIB(strFileName=r"\\NetworkMachine\shared _folder\sample.mlib")
```
