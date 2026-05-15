---
title: "WatchSelectedDataSaveToFile()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Save information of watch data docking window.

## Syntax

```psj
WatchSelectedDataSaveToFile(string csvFilePath)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. string

Path of save file (.csv)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
WatchSelectedDataSaveToFile("C:/Temp/sample.csv")
```
