---
title: "AddResultsADVC()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Add ADVC results to the current Jupiter Database.

## Syntax

```psj
AddResultsADVC(str[] strlPaths, bool bMergeTree, bool bADVCProcessNameRule, bool bDisplayNAResult, str strPathSelectResultFile)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. str\[]

- A List of String specifying a list of the ADVC files which will be used for importing.

<!-- @since:5.1.0 -->
### 2. bool

- A Boolean specifying whether or not the differences not included in the existing document will be added.

<!-- @since:5.1.0 -->
### 3. bool

- A Boolean specifying whether or not ADVC process IDs defined on the ADVC side are displayed.

<!-- @since:5.1.0 -->
### 4. bool

- A Boolean specifying whether or not the "NA Result Display" option in ADVC is enabled. When set to true, it shows "Data: ---" for missing data and "No data available" in watch data notes, applicable only to nodal output results. When set to false, standard data display rules apply.

<!-- @since:5.1.0 -->
### 5. str

- A String specifying path to the results file.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
AddResultsADVC(["path/to/the/file"], 1, 1, 1, "")
```
