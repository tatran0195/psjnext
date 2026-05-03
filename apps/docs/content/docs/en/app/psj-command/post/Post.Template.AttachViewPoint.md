---
title: "Post.Template.AttachViewPoint()"
description: "Attach the current view point settings to the specified template"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > Template > AttachViewPoint"
macro_link: "[AttachTemplateViewPoint](../../macro/post/AttachTemplateViewPoint)"
---

## Description

Attach the current view point settings to the specified template

## Syntax

```psj
Post.Template.AttachViewPoint(...)
```

## Inputs

### `strName` @type(String) @default("NewTemplate")

- Specifying the name of template, which will attach the viewpoint settings.

### `postDataVizOptViewPoint` @type(POST\_DATA\_VIZ\_OPT\_VIEWPOINT) @default(POST\_DATA\_VIZ\_OPT\_VIEWPOINT)

- All settings of a view point.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {2-6}
Post.Template.Create(strName="ViewPoint_Template", strComment="Attach View Point Template")
template = Post.Template.AttachViewPoint(strName="ViewPoint_Template", 
                                        postDataVizOptViewPoint=POST_DATA_VIZ_OPT_VIEWPOINT(
                                            dlTranslationMatrix=[-0.707107, -0.5, 0.5, 0.0, 0.707107, -0.5, 0.5, 0.0, -4.49147e-08, 0.707107, 0.707107, 0.0, 0.0, 0.0, 0.0, 1.0], 
                                            dlCenter=[0.016, 0.005, 0.0025], 
                                            dScaleFactor=0.0115058))
JPT.Debugger(template)
```
