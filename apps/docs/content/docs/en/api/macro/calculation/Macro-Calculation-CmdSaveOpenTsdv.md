---
title: "CmdSaveOpenTsdv()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Save or load the results of a frequency response analysis (\*.tsdv).

## Syntax

```psj
CmdSaveOpenTsdv(str strFilePath, int  iSaveOpenMode, cursor crlTargetItems, bool bBdfMode, int iAnalysisType)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. str

- A String specifying the path of file will be saved or opened.

<!-- @since:5.1.0 -->
### 2. int

- 0 if save mode or 1 if load mode.

<!-- @since:5.1.0 -->
### 3. cursor

- A List of Cursor specifying the specified analysis targets to be saved if save mode or \[] if load mode.

<!-- @since:5.1.0 -->
### 4. bool

- A Boolean specifying whether to use the BDF mode.

<!-- @since:5.1.0 -->
### 5. int

- 0 if Frequency response or 1 if transient response.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CmdSaveOpenTsdv("path/to/the/file", 0, [0:0], 1, 0)
```
