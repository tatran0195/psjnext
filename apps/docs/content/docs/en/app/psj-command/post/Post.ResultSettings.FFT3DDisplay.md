---
title: "Post.ResultSettings.FFT3DDisplay()"
description: "Set up the result settings for displaying the FFT3D"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > ResultSettings > FFT3DDisplay"
macro_link: "[CmdPostFFT3DDisplaySettings](../../macro/post/CmdPostFFT3DDisplaySettings)"
---

## Description

Set up the result settings for displaying the FFT3D.

## Syntax

```psj
Post.ResultSettings.FFT3DDisplay(...)
```

## Inputs

### `postDataVizOptBDPP` @type(POST\_DATA\_VIZ\_OPT\_BDPP) @default(POST\_DATA\_VIZ\_OPT\_BDPP)

- All settings of the FFT3D display.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {1-5}
Post.ResultSettings.FFT3DDisplay(postDataVizOptBDPP=PostDataVizOptBDPP(
                                dLayerPointSize=2.0, 
                                dLineWidth=2.0, 
                                dPointSize=2.0, 
                                dDotDistance=0.05))
```
