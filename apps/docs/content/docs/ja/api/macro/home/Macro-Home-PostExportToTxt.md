---
title: "PostExportToTxt()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Export results to .txt file.

## Syntax

```psj
PostExportToTxt(str strFileName, int iSpliterType, bool bAppend, cursor[] crlJobs, int[] ilAnalysisTypes, int[] ilResultSets, int[] ilTimeSteps, int[] ilResultTypes, int[] ilResultPos, str[] strlResultNames, str[] strlCompNames, str[] strlNames, str[] strlTypes, cursor[] crlEdit)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. str

- A string specifying file name.

<!-- @since:5.1.0 -->
### 2. int

- An integer specifying the type of delimiter.

<!-- @since:5.1.0 -->
### 3. bool

- A boolean specifying whether to append the data.

<!-- @since:5.1.0 -->
### 4. cursor\[]

- A list of cursor specifying the jobs.

<!-- @since:5.1.0 -->
### 5. int\[]

- A list of integers specifying the types of analysis.

<!-- @since:5.1.0 -->
### 6. int\[]

- A list of integers specifying the result sets.

<!-- @since:5.1.0 -->
### 7. int\[]

- A list of integers specifying the time steps.

<!-- @since:5.1.0 -->
### 8. int\[]

- An list of integers specifying the types of results.

<!-- @since:5.1.0 -->
### 9. int\[]

- A list of integers specifying the positions of the results.

<!-- @since:5.1.0 -->
### 10. str\[]

- A list of strings specifying the names of the results.

<!-- @since:5.1.0 -->
### 11. str\[]

- A list of strings specifying the names of the components.

<!-- @since:5.1.0 -->
### 12. str\[]

- A list of strings specifying names.

<!-- @since:5.1.0 -->
### 13. str\[]

- A list of strings specifying types.

<!-- @since:5.1.0 -->
### 14. cursor\[]

- A list of cursor specifying edit.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
PostExportToTxt("strFileName", 0, 0, [], [], [], [], [], [], [], [], [], [], [])
```
