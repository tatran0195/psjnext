---
title: "ResultOutputList()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Export the selected results to a CSV file or a universal format.

## Syntax

```psj
ResultOutputList(string PathFile, cursor[] Bodies, int ResultType, int Output, int OutPutType, int Target, bool MidNode, int[] PostResultKeyAnalysis, int[] PostResultKeyResultSet, int[] PostResultKeyTimeStep, int[] PostResultKeyCatType)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. String

A String specifying the file path to be exported.

<!-- @since:5.1.0 -->
### 2. Cursor\[]

A Cursor List specifying the selected parts to be exported data.

<!-- @since:5.1.0 -->
### 3. Int

An Integer specifying the result type to be exported.

<!-- @since:5.1.0 -->
### 4. Int

An Integer specifying to output all selected subcases in one file or in separated files for each selected subcase.

<!-- @since:5.1.0 -->
### 5. Int

An Integer specifying the format of the output file.

<!-- @since:5.1.0 -->
### 6. Int

An Integer specifying the output position of the result.

<!-- @since:5.1.0 -->
### 7. Bool

A Boolean specifying whether to enable/disable middle node for the exported results.

<!-- @since:5.1.0 -->
### 8. Int\[]

A List specifying the attributes of the selected result.

<!-- @since:5.1.0 -->
### 9. Int\[]

A List specifying the attributes for the set of the selected results.

<!-- @since:5.1.0 -->
### 10. Int\[]

A List specifying the attributes for the time step of the selected results.

<!-- @since:5.1.0 -->
### 11. Int\[]

A List specifying the attributes for the cat type of the selected results.

## Return Code

- "1": The function can be executed.
- "0": The function cannot be executed.

## Sample Code

```psj
ResultOutputList("C:/temp/file.csv", [3:7, 3:8, 3:9, 3:2], 7, 0, 0, 0, 1, [1, 1, 1], [0, 0, 0], [0, 2, 4], [0, 0, 0])
```
