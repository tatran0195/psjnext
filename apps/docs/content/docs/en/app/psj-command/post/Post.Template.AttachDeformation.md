---
title: "Post.Template.AttachDeformation()"
description: "Attach the current deformation settings to the specified template"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > Template > AttachDeformation"
macro_link: "[AttachTemplateDeformation](../../macro/post/AttachTemplateDeformation)"
---

## Description

Attach the current deformation settings to the specified template.

## Syntax

```psj
Post.Template.AttachDeformation(...)
```

## Inputs

### `strName` @type(String) @default("NewTemplate")

- The name of template, which will attach the deformation settings.

### `postDataVizOptDeform` @type(POST\_DATA\_VIZ\_OPT\_DEFORM) @default(POST\_DATA\_VIZ\_OPT\_DEFORM)

- All settings of the deformation display.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {2-5}
Post.Template.Create(strName="Deformation_Template", strComment="Attach Deformation Template")
template = Post.Template.AttachDeformation(strName="Deformation_Template", 
                                        postDataVizOptDeform=POST_DATA_VIZ_OPT_DEFORM(
                                            bEachDirectionRatio=True, 
                                            dlEachDirectionRatio=[0.05, 0.05, 0.05]))
JPT.Debugger(template)
```
