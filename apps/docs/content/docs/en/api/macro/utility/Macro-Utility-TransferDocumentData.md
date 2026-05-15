---
title: "TransferDocumentData()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Transfer items in a document to another document.

## Syntax

```psj
TransferDocumentData(string strSourceDocTitle, string strDestDocTitle, cursor[] Parts, string[] strlNewPartName, cursor crDestAssemblyInstance, bool bEnableCutOperation)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. String

The name of source document.

<!-- @since:5.1.0 -->
### 2. String

The name of destination document.

<!-- @since:5.1.0 -->
### 3. cursor\[]

A List of Cursor specifying the transformed parts.

<!-- @since:5.1.0 -->
### 4. String\[]

A List of the new names of transformed parts in the destination document.

<!-- @since:5.1.0 -->
### 5. Cursor

The name of destination document.

<!-- @since:5.1.0 -->
### 6. Bool

Specify cut or copy.

- 0: cut.
- 1: copy.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
TransferDocumentData("Jupiter1", "Jupiter2", [3:1], ["Cube _1"], 0:0, 1)
```
