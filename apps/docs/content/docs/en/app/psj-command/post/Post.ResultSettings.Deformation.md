---
title: "Post.ResultSettings.Deformation()"
description: "Set up the result settings for displaying the deformation"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > ResultSettings > Deformation"
macro_link: "[CmdPostDeformSettings](../../macro/post/CmdPostDeformSettings)"
---

## Description

Set up the result settings for displaying the deformation.

## Syntax

```psj
Post.ResultSettings.Deformation(...)
```

## Inputs

### `postDataVizOptDeform` @type(POST\_DATA\_VIZ\_OPT\_DEFORM) @default(POST\_DATA\_VIZ\_OPT\_DEFORM)

- All settings of the deformation display.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {1}
Post.ResultSettings.Deformation(postDataVizOptDeform=PostDataVizOptDeform(bEachDirectionRatio=True))
```
