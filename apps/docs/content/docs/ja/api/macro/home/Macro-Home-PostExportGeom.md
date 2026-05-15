---
title: "PostExportGeom()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Export geometry surface.

## Syntax

```psj
PostExportGeom(str strFolderName, bool bUseUnit)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. str

- A string specifying the path to forder name.

<!-- @since:5.1.0 -->
### 2. bool

- A boolean specifying whether or not use unit.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
PostExportGeom("path/to/the/folder", 1)
```
