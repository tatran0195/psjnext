---
title: "ImportVDB()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Import TSV VDB file

## Syntax

```psj
ImportVDB(string SourceFilePath, string SaveFolderPath)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Path of file to import

<!-- @since:5.0.1 -->
### 2. String

Path directory to save

:::note
If this parameter is not indicated, converted files are saved under Temp folder.
:::

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImportVDB("D:/Source.vdb","D:/ConvertedMyFile/")
```
