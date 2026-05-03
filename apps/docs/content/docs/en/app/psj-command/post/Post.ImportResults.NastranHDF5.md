---
title: "Post.ImportResults.NastranHDF5()"
description: "Import Nastran HDF5PostJob file"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Post > ImportResults > NastranHDF5"
---

## Description

Import Nastran HDF5PostJob file

## Syntax

```psj
Post.ImportResults.NastranHDF5(strName="", strlPaths=[], crEdit=None)
```

## Inputs

### `strName` @type(String) @default("")

- The name.

### `strlPaths` @type(List\[String]) @default(\[])

- The paths.

### `crEdit` @type(Cursor) @default(None)

- The cursor of Result Nastran HDF5 needs editing.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Post.ImportResults.NastranHDF5(strName="", strlPaths=[], crEdit=None)
```
