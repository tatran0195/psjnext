---
title: "ContourCopy()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Display the contour of the current Post document in the specified Pre document.

## Syntax

```psj
ContourCopy(string PostDocName, string PreDocName)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. String

A String specifying the Post document name to copy the contour.

<!-- @since:5.1.0 -->
### 2. String

A String specifying the Pre document name to be copied the contour.

## Return Code

- "1": The function can be executed.
- "0": The function cannot be executed.

## Sample Code

```psj
ContourCopy("101 _solid", "101 _solid _Converted _Pre")
```
