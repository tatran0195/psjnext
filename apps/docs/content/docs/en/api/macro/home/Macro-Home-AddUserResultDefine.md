---
title: "AddUserResultDefine()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Add user result to the current Jupiter Database.

## Syntax

```psj
UsersResult(str[] strlPath, bool bExportLog)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. str\[]

- A List of String specifying user result files.

<!-- @since:5.1.0 -->
### 2. bool

- A Boolean specifying whether or not

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
UsersResult(["path/to/the/file"], 1)
```
