---
title: "Post.Template.AttachCircle()"
description: "Attach the current result circle settings to the specified template"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > Template > AttachCircle"
macro_link: "[AttachTemplateCircle](../../macro/post/AttachTemplateCircle)"
---

## Description

Attach the current result circle settings to the specified template.

## Syntax

```psj
Post.Template.AttachCircle(...)
```

## Inputs

### `strName` @type(String) @default("NewTemplate")

- The name of template, which will attach the circle settings.

### `postDataVizOptCircle` @type(POST\_DATA\_VIZ\_OPT\_CIRCLE) @default(POST\_DATA\_VIZ\_OPT\_CIRCLE)

- All settings of the circle display.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {2-5}
Post.Template.Create(strName="Circle_Template", strComment="Attach Circle Template")
template = Post.Template.AttachCircle(strName="Circle_Template", 
                                    postDataVizOptCircle=POST_DATA_VIZ_OPT_CIRCLE(
                                        dRatioModel=0.04, 
                                        dRatioScreen=0.04))
JPT.Debugger(template)
```
