---
title: "Post.Template.AttachDeformation()"
description: "Attach the current deformation settings to the specified template"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > Template > AttachDeformation"
macro _link: "[AttachTemplateDeformation](../../macro/post/AttachTemplateDeformation)"
---

## Description

Attach the current deformation settings to the specified template.

## Syntax

```psj
Post.Template.AttachDeformation(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @optional @default:"NewTemplate" -->
### `strName`

- The name of template, which will attach the deformation settings.

<!-- @since:5.1.0 @type:POST _DATA _VIZ _OPT _DEFORM @optional @default:POST _DATA _VIZ _OPT _DEFORM -->
### `postDataVizOptDeform`

- The all settings of the deformation display.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {2-5}
Post.Template.Create(strName="Deformation _Template", strComment="Attach Deformation Template")
template = Post.Template.AttachDeformation(strName="Deformation _Template", 
                                        postDataVizOptDeform=POST _DATA _VIZ _OPT _DEFORM(
                                            bEachDirectionRatio=True, 
                                            dlEachDirectionRatio=[0.05, 0.05, 0.05]))
JPT.Debugger(template)
```
