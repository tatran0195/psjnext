---
title: "Post.ResultSettings.Opacity()"
description: "Set up the result settings for displaying the opacity"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > ResultSettings > Opacity"
macro _link: "[CmdPostTransparencySettings](../../macro/post/CmdPostTransparencySettings)"
---

## Description

Set up the result settings for displaying the opacity.

## Syntax

```psj
Post.ResultSettings.Opacity(...)
```

## Inputs

<!-- @since:5.1.0 @type:POST _DATA _VIZ _OPT _TRANSPARENCY @optional @default:POST _DATA _VIZ _OPT _TRANSPARENCY -->
### `postDataVizOptTransparency`

- The all settings of the opacity display.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {1}
Post.ResultSettings.Opacity(postDataVizOptTransparency=PostDataVizOptTransparency(dTransparency=0.5))
```
