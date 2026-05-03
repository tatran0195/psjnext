---
title: "Assembly.RightClick.Rename()"
description: "Rename a specified entity"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Assembly > RightClick > Rename"
macro_link: "RenameItem"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Rename a specified entity.

## Syntax

```psj
Assembly.RightClick.Rename(...)
```

## Inputs

### `strNewName` @type(String) @default("New name")

- The new name for item.

### `crItem` @type(Cursor) @required

- The item which name will be changed.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {3,4}
Geometry.Part.Cube()

rename_status = Assembly.RightClick.Rename(strNewName="Box", 
                                           crItem=Part(1))

JPT.Debugger(rename_status)
```
