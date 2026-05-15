---
title: "Post.ResultSettings.Title()"
description: "Set up the result settings for displaying the title"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > ResultSettings > Title"
macro _link: "[CmdPostTitleSettings](../../macro/post/CmdPostTitleSettings)"
---

## Description

Set up the result settings for displaying the title.

## Syntax

```psj
Post.ResultSettings.Title(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### postDataVizOptTitle

- Specify all settings of the result title display.
- The default value is [POST\_DATA\_VIZ\_OPT\_TITLE](../../data-type/psj-command/parameter-types/POST _DATA _VIZ _OPT _TITLE).

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {1}
Post.ResultSettings.Title(postDataVizOptTitle=PostDataVizOptTitle(iBackgroundFillColor=17919, dTransparency=0.6))
```
