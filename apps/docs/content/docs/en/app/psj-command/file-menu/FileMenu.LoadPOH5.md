---
title: "FileMenu.LoadPOH5()"
description: "Open .poh5 / .poh5a file."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "FileMenu > LoadPOH5"
---

## Description

Open .poh5 / .poh5a file.

## Syntax

```psj
FileMenu.LoadPOH5(...)
```

## Inputs

### `strFileName` @type(String) @required

- The file name.

### `iSaveOption` @type(Integer)

- The save option.
- It always set 0 for this function.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj{3}
# Prepare a poh5 / poh5a file to read
poh5_filepath = "C:/temp/mydata.poh5"

FileMenu.LoadPOH5(poh5_filepath)
```
