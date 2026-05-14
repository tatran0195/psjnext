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

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strFileName`

- The file name.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bUseTmpTable`

- The use temporary table.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
FileMenu.Open(strFileName="", bUseTmpTable=False)
```
