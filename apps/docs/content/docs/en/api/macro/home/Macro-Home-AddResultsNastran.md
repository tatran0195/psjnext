---
title: "AddResultsNastran()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Add Nastran Op2 results to the current Jupiter Database. The Jupiter document should be Post document.

## Syntax

```psj
AddResultsNastran(str[] strlPaths, bool bMergeTree, bool bCreateResultAtMidNode)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. str\[]

- A List of String specifying a list of the Nastran files (\*.op2 files) which will be used for importing.

<!-- @since:5.1.0 -->
### 2. bool

- A Boolean specifying whether or not the differences not included in the existing document will be added.

<!-- @since:5.1.0 -->
### 3. bool

- A Boolean specifying whether or not create result at Mid Nodes.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
AddResultsNastran(["path/to/the/file"], 1, 1)
```
