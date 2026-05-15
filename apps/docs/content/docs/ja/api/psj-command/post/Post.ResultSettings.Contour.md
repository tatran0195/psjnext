---
title: "Post.ResultSettings.Contour()"
description: "Set up the result settings for displaying the contour"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > ResultSettings > Contour"
macro _link: "[CmdPostContourSettings](../../macro/post/CmdPostContourSettings)"
---

## Description

Set up the result settings for displaying the contour.

## Syntax

```psj
Post.ResultSettings.Contour(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### postDataVizOptContour

- Specify all settings of the contour display.
- The default value is [POST\_DATA\_VIZ\_OPT\_CONTOUR](../../data-type/psj-command/parameter-types/POST _DATA _VIZ _OPT _CONTOUR).

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {1-6}
Post.ResultSettings.Contour(postDataVizOptContour=PostDataVizOptContour(
                            dMaxUser=1696.404297, 
                            dMinUser=0.0, 
                            dMaxTotal=1696.404297, 
                            dMinTotal=0.0, 
                            iInterpolateMethod=-1))
```
