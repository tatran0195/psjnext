---
title: "Post.ResultSettings.Animation()"
description: "Set up the result settings for displaying the animation"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > ResultSettings > Animation"
macro _link: "[CmdPostAnimationSettings](../../macro/post/CmdPostAnimationSettings)"
---

## Description

Set up the result settings for displaying the animation.

## Syntax

```psj
Post.ResultSettings.Animation(...)
```

## Inputs

<!-- @since:5.1.0 @type:POST _DATA _VIZ _OPT _ANIMATION @optional @default:POST _DATA _VIZ _OPT _ANIMATION -->
### `postDataVizOptAnimation`

- The all settings of the animation display.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {1}
Post.ResultSettings.Animation(postDataVizOptAnimation=PostDataVizOptAnimation(iLoopType=2, bFixContour=True))
```
