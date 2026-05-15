---
title: "Post.ResultSettings.Deformation()"
description: "Set up the result settings for displaying the deformation"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > ResultSettings > Deformation"
macro _link: "[CmdPostDeformSettings](../../macro/post/CmdPostDeformSettings)"
---

## Description

Set up the result settings for displaying the deformation.

## Syntax

```psj
Post.ResultSettings.Deformation(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### postDataVizOptDeform

- Specify all settings of the deformation display.
- The default value is [POST\_DATA\_VIZ\_OPT\_DEFORM](../../data-type/psj-command/parameter-types/POST _DATA _VIZ _OPT _DEFORM).

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {1}
Post.ResultSettings.Deformation(postDataVizOptDeform=PostDataVizOptDeform(bEachDirectionRatio=True))
```
