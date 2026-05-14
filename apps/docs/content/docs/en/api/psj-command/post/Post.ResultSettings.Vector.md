---
title: "Post.ResultSettings.Vector()"
description: "Set up the result settings for displaying the vector"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > ResultSettings > Vector"
macro _link: "[CmdPostVectorSettings](../../macro/post/CmdPostVectorSettings)"
---

## Description

Set up the result settings for displaying the vector.

## Syntax

```psj
Post.ResultSettings.Vector(...)
```

## Inputs

<!-- @since:5.1.0 @type:POST _DATA _VIZ _OPT _VECTOR @optional @default:POST _DATA _VIZ _OPT _VECTOR -->
### `postDataVizOptVector`

- The all settings of the result vector display.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {1}
Post.ResultSettings.Vector(postDataVizOptVector=PostDataVizOptVector(dRatioModel=0.05, dRatioScreen=0.05))
```
