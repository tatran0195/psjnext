---
title: "Post.Template.AttachAnimation()"
description: "Attach the current animation settings to the specified template"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > Template > AttachAnimation"
macro_link: "[AttachTemplateAnimation](../../macro/post/AttachTemplateAnimation)"
---

## Description

Attach the current animation settings to the specified template.

## Syntax

```psj
Post.Template.AttachAnimation(...)
```

## Inputs

### `strName` @type(String) @default("NewTemplate")

- The name of template, which will attach the animation settings.

### `postDataVizOptAnimation` @type(POST\_DATA\_VIZ\_OPT\_ANIMATION) @default(POST\_DATA\_VIZ\_OPT\_ANIMATION)

- All settings of the animation display.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {2-7}
Post.Template.Create(strName="Animation_Template", strComment="Attach Animation Template")
template = Post.Template.AttachAnimation(strName="Animation_Template", 
                                        postDataVizOptAnimation=POST_DATA_VIZ_OPT_ANIMATION(
                                            iFPS=10, 
                                            iFrameNumber=10, 
                                            iLoopType=0, 
                                            bPhaseAngle=True))
JPT.Debugger(template)
```
