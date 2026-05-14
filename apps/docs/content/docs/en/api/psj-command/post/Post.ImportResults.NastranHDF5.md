---
title: "Post.ImportResults.NastranHDF5()"
description: "Import Nastran HDF5PostJob file"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Post > ImportResults > NastranHDF5"
---

## Description

Import Nastran HDF5PostJob file

## Syntax

```psj
Post.ImportResults.NastranHDF5(strName="", strlPaths=[], crEdit=None)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:List[String] @optional @default:[] -->
### `strlPaths`

- The paths.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The cursor of Result Nastran HDF5 needs editing.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Post.ImportResults.NastranHDF5(strName="", strlPaths=[], crEdit=None)
```
