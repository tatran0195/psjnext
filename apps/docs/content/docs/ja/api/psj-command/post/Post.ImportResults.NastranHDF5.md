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

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### strlPaths

- Specify the paths.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the cursor of Result Nastran HDF5 needs editing.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Post.ImportResults.NastranHDF5(strName="", strlPaths=[], crEdit=None)
```
