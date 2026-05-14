---
title: "Post.Template.AttachViewPoint()"
description: "Attach the current view point settings to the specified template"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > Template > AttachViewPoint"
macro _link: "[AttachTemplateViewPoint](../../macro/post/AttachTemplateViewPoint)"
---

## Description

Attach the current view point settings to the specified template

## Syntax

```psj
Post.Template.AttachViewPoint(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @optional @default:"NewTemplate" -->
### `strName`

- The specifying the name of template, which will attach the viewpoint settings.

<!-- @since:5.1.0 @type:POST _DATA _VIZ _OPT _VIEWPOINT @optional @default:POST _DATA _VIZ _OPT _VIEWPOINT -->
### `postDataVizOptViewPoint`

- The all settings of a view point.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {2-6}
Post.Template.Create(strName="ViewPoint _Template", strComment="Attach View Point Template")
template = Post.Template.AttachViewPoint(strName="ViewPoint _Template", 
                                        postDataVizOptViewPoint=POST _DATA _VIZ _OPT _VIEWPOINT(
                                            dlTranslationMatrix=[-0.707107, -0.5, 0.5, 0.0, 0.707107, -0.5, 0.5, 0.0, -4.49147e-08, 0.707107, 0.707107, 0.0, 0.0, 0.0, 0.0, 1.0], 
                                            dlCenter=[0.016, 0.005, 0.0025], 
                                            dScaleFactor=0.0115058))
JPT.Debugger(template)
```
