---
title: "AddResultsActran()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Add Actran Op2 results to the current Jupiter Database. The Jupiter document should be Post document.

## Syntax

```psj
AddResultsActran(str[] strlPaths, bool bMergeTree)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. str\[]

- A List of String specifying a list of the Actran files (\*.op2 files) which will be used for importing.

<!-- @since:5.1.0 -->
### 2. bool

- A Boolean specifying whether or not the differences not included in the existing document will be added.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
AddResultsActran(["path/to/the/file"], 1)
```
