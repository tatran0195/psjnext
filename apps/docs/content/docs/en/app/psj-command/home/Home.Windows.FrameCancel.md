---
title: "Home.Windows.FrameCancel()"
description: "Reset placement of document windows to the original."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > Windows > Cancel"
macro_link: "[FrameLessCancel](../../macro/home/FrameLessCancel)"
---

## Description

Reset placement of document windows to the original (full window).

## Syntax

```psj
Home.Windows.FrameCancel(...)
```

## Inputs

This function does not require any input value.

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not.
  - True: The function successfully executed.
  - False: The function cannot be executed.

## Sample Code

```psj {7}
# Prepare 2 JPT documents
JPT.CreateNewDocument()
JPT.CreateNewDocument()
Home.Windows.TileHorizontal(iMode=0)

# Cancel to the full window display.
Home.Windows.FrameCancel()
```
