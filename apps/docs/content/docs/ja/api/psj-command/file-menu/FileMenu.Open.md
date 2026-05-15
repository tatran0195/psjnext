---
title: "FileMenu.Open()"
description: "Load JTDB file"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "FileMenu > Open"
---

## Description

Load JTDB file

## Syntax

```psj
FileMenu.Open(strFileName="", bUseTmpTable=False)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strFileName

- Specify the file name.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### bUseTmpTable

- Specify the use temporary table.
- The default value is False.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
FileMenu.Open(strFileName="", bUseTmpTable=False)
```
