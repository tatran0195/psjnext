---
title: "FileMenu.Save()"
description: "Save file JTDB"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "FileMenu > Save"
---

## Description

Save file JTDB

## Syntax

```psj
FileMenu.Save(strFileName="")
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strFileName

- Specify the file name.
- The default value is "".

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
FileMenu.Save(strFileName="")
```
