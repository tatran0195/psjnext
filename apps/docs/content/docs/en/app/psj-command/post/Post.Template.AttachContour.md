---
title: "Post.Template.AttachContour()"
description: "Attach the current contour settings to the specified template"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > Template > AttachContour"
macro_link: "[AttachTemplateContour](../../macro/post/AttachTemplateContour)"
---

## Description

Attach the current contour settings to the specified template.

## Syntax

```psj
Post.Template.AttachContour(...)
```

## Inputs

### `strName` @type(String) @default("NewTemplate")

- The name of Template will attach the contour settings.

### `postDataVizOptContour` @type(POST\_DATA\_VIZ\_OPT\_CONTOUR) @default(POST\_DATA\_VIZ\_OPT\_CONTOUR)

- All settings of the contour display.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {2-6}
Post.Template.Create(strName="Contour_Template", strComment="Attach Contour Template")
template = Post.Template.AttachContour(strName="Contour_Template", 
                                    postDataVizOptContour=POST_DATA_VIZ_OPT_CONTOUR(
                                        iColorDivision=20, 
                                        dMaxUser=0, 
                                        dMinUser=0))
JPT.Debugger(template)
```
