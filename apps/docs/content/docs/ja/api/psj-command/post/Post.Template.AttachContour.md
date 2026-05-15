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

<!-- @since:5.1.0 @optional -->
### strName

- Specify the name of Template will attach the contour settings.
- The default value is "NewTemplate".

<!-- @since:5.1.0 @optional -->
### postDataVizOptContour

- Specify all settings of the contour display.
- The default value is [POST\_DATA\_VIZ\_OPT\_CONTOUR](../../data-type/psj-command/parameter-types/POST _DATA _VIZ _OPT _CONTOUR).

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
