---
title: "Post.ResultSettings.Circle()"
description: "Set up the result settings for displaying the circle"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > ResultSettings > Circle"
macro _link: "[CmdPostCircleSettings](../../macro/post/CmdPostCircleSettings)"
---

## Description

Set up the result settings for displaying the circle.

## Syntax

```psj
Post.ResultSettings.Circle(...)
```

## Inputs

<!-- @since:5.1.0 @type:POST _DATA _VIZ _OPT _CIRCLE @optional @default:POST _DATA _VIZ _OPT _CIRCLE -->
### `postDataVizOptCircle`

- The all settings of the circle display.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {1}
Post.ResultSettings.Circle(postDataVizOptCircle=PostDataVizOptCircle(dRatioModel=0.05, dRatioScreen=0.05))
```
