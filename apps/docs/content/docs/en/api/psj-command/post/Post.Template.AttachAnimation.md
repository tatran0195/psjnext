---
title: "Post.Template.AttachAnimation()"
description: "Attach the current animation settings to the specified template"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > Template > AttachAnimation"
macro _link: "[AttachTemplateAnimation](../../macro/post/AttachTemplateAnimation)"
---

## Description

Attach the current animation settings to the specified template.

## Syntax

```psj
Post.Template.AttachAnimation(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @optional @default:"NewTemplate" -->
### `strName`

- The name of template, which will attach the animation settings.

<!-- @since:5.1.0 @type:POST _DATA _VIZ _OPT _ANIMATION @optional @default:POST _DATA _VIZ _OPT _ANIMATION -->
### `postDataVizOptAnimation`

- The all settings of the animation display.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {2-7}
Post.Template.Create(strName="Animation _Template", strComment="Attach Animation Template")
template = Post.Template.AttachAnimation(strName="Animation _Template", 
                                        postDataVizOptAnimation=POST _DATA _VIZ _OPT _ANIMATION(
                                            iFPS=10, 
                                            iFrameNumber=10, 
                                            iLoopType=0, 
                                            bPhaseAngle=True))
JPT.Debugger(template)
```
