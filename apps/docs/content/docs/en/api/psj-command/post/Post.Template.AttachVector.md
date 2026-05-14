---
title: "Post.Template.AttachVector()"
description: "Attach the current vector settings to the specified template"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > Template > AttachVector"
macro _link: "[AttachTemplateVector](../../macro/post/AttachTemplateVector)"
---

## Description

Attach the current vector settings to the specified template.

## Syntax

```psj
Post.Template.AttachVector(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @optional @default:"NewTemplate" -->
### `strName`

- The name of template, which will attach the vector settings.

<!-- @since:5.1.0 @type:POST _DATA _VIZ _OPT _VECTOR @optional @default:POST _DATA _VIZ _OPT _VECTOR -->
### `postDataVizOptVector`

- The all settings of the result vector display.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {2-5}
Post.Template.Create(strName="Vector _Template", strComment="Attach Vector Template")
template = Post.Template.AttachVector(strName="Vector _Template", 
                                    postDataVizOptVector=POST _DATA _VIZ _OPT _VECTOR(
                                        dRatioModel=0.05, 
                                        dRatioScreen=0.05))
JPT.Debugger(template)
```
