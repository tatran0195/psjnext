---
title: "SaveMPCResultToCSV()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Save MPC Result To CSV file.

## Syntax

```psj
SaveMPCResultToCSV(cursor crResponse, double dTime, str strFilePath)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. cursor

- A Cursor specifying the response to be saved.

<!-- @since:5.1.0 -->
### 2. double

- A Double specifying the time at which the result will be saved.

<!-- @since:5.1.0 -->
### 3. str

- A String specifying the path of CSV file to be saved.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
SaveMPCResultToCSV(0:0, 0.0, "path/to/the/file")
```
