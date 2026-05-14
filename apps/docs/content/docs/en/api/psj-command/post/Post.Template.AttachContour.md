---
title: "Post.Template.AttachContour()"
description: "Attach the current contour settings to the specified template"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > Template > AttachContour"
macro _link: "[AttachTemplateContour](../../macro/post/AttachTemplateContour)"
---

## Description

Attach the current contour settings to the specified template.

## Syntax

```psj
Post.Template.AttachContour(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @optional @default:"NewTemplate" -->
### `strName`

- The name of Template will attach the contour settings.

<!-- @since:5.1.0 @type:POST _DATA _VIZ _OPT _CONTOUR @optional @default:POST _DATA _VIZ _OPT _CONTOUR -->
### `postDataVizOptContour`

- The all settings of the contour display.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {2-6}
Post.Template.Create(strName="Contour _Template", strComment="Attach Contour Template")
template = Post.Template.AttachContour(strName="Contour _Template", 
                                    postDataVizOptContour=POST _DATA _VIZ _OPT _CONTOUR(
                                        iColorDivision=20, 
                                        dMaxUser=0, 
                                        dMinUser=0))
JPT.Debugger(template)
```
