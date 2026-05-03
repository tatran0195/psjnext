---
title: "Post.ResultSettings.Title()"
description: "Set up the result settings for displaying the title"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > ResultSettings > Title"
macro_link: "[CmdPostTitleSettings](../../macro/post/CmdPostTitleSettings)"
---

## Description

Set up the result settings for displaying the title.

## Syntax

```psj
Post.ResultSettings.Title(...)
```

## Inputs

### `postDataVizOptTitle` @type(POST\_DATA\_VIZ\_OPT\_TITLE) @default(POST\_DATA\_VIZ\_OPT\_TITLE)

- All settings of the result title display.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {1}
Post.ResultSettings.Title(postDataVizOptTitle=PostDataVizOptTitle(iBackgroundFillColor=17919, dTransparency=0.6))
```
