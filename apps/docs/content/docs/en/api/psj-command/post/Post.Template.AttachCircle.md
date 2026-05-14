---
title: "Post.Template.AttachCircle()"
description: "Attach the current result circle settings to the specified template"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > Template > AttachCircle"
macro _link: "[AttachTemplateCircle](../../macro/post/AttachTemplateCircle)"
---

## Description

Attach the current result circle settings to the specified template.

## Syntax

```psj
Post.Template.AttachCircle(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @optional @default:"NewTemplate" -->
### `strName`

- The name of template, which will attach the circle settings.

<!-- @since:5.1.0 @type:POST _DATA _VIZ _OPT _CIRCLE @optional @default:POST _DATA _VIZ _OPT _CIRCLE -->
### `postDataVizOptCircle`

- The all settings of the circle display.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {2-5}
Post.Template.Create(strName="Circle _Template", strComment="Attach Circle Template")
template = Post.Template.AttachCircle(strName="Circle _Template", 
                                    postDataVizOptCircle=POST _DATA _VIZ _OPT _CIRCLE(
                                        dRatioModel=0.04, 
                                        dRatioScreen=0.04))
JPT.Debugger(template)
```
