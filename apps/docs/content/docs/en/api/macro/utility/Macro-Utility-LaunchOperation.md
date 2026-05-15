---
title: "LaunchOperation()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Launch indicated command dialog

## Syntax

```psj
LaunchOperation(string strCommandID, int iPattern)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. String

Command ID (name of the command)

<!-- @since:5.1.0 -->
### 2. int

Indicate pattern if the command has several display pattern.

## Return Code

- "1": The function can be executed
- "FAILED": The function cannot be executed

## Sample Code

```psj
LaunchOperation("GEOMETRY _CREATE _ENTITY _PARTS _CUBE", 0)
```
