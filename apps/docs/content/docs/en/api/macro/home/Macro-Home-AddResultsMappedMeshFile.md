---
title: "AddResultsMappedMeshFile()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Add mapped mesh result to the current Jupiter Database.

## Syntax

```psj
AddResultsMappedMeshFile(str[] strlPaths, bool bMergeTree)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. str\[]

- A List of String specifying mapped mesh files.

<!-- @since:5.1.0 -->
### 2. bool

- A Boolean specifying whether or not the differences not included in the existing document will be added.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
AddResultsMappedMeshFile(["path/to/the/file"], 1)
```
