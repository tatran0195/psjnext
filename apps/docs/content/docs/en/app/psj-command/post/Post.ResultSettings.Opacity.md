---
title: "Post.ResultSettings.Opacity()"
description: "Set up the result settings for displaying the opacity"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > ResultSettings > Opacity"
macro_link: "[CmdPostTransparencySettings](../../macro/post/CmdPostTransparencySettings)"
---

## Description

Set up the result settings for displaying the opacity.

## Syntax

```psj
Post.ResultSettings.Opacity(...)
```

## Inputs

### `postDataVizOptTransparency` @type(POST\_DATA\_VIZ\_OPT\_TRANSPARENCY) @default(POST\_DATA\_VIZ\_OPT\_TRANSPARENCY)

- All settings of the opacity display.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {1}
Post.ResultSettings.Opacity(postDataVizOptTransparency=PostDataVizOptTransparency(dTransparency=0.5))
```
