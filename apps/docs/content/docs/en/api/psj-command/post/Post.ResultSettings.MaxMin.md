---
title: "Post.ResultSettings.MaxMin()"
description: "Set up the result settings for displaying Max/Min value"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > ResultSettings > MaxMin"
macro _link: "[CmdPostMaxMinSettings](../../macro/post/CmdPostMaxMinSettings)"
---

## Description

Set up the result settings for displaying Max/Min value.

## Syntax

```psj
Post.ResultSettings.MaxMin(...)
```

## Inputs

<!-- @since:5.1.0 @type:POST _DATA _VIZ _OPT _MAXMIN @optional @default:POST _DATA _VIZ _OPT _MAXMIN -->
### `postDataVizOptMaxMin`

- The all settings to display Max/Min value.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {1}
Post.ResultSettings.MaxMin(postDataVizOptMaxMin=PostDataVizOptMaxMin(iGroupMethod=1))
```
