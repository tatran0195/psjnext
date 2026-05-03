---
title: "Post.Template.AttachVector()"
description: "Attach the current vector settings to the specified template"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > Template > AttachVector"
macro_link: "[AttachTemplateVector](../../macro/post/AttachTemplateVector)"
---

## Description

Attach the current vector settings to the specified template.

## Syntax

```psj
Post.Template.AttachVector(...)
```

## Inputs

### `strName` @type(String) @default("NewTemplate")

- The name of template, which will attach the vector settings.

### `postDataVizOptVector` @type(POST\_DATA\_VIZ\_OPT\_VECTOR) @default(POST\_DATA\_VIZ\_OPT\_VECTOR)

- All settings of the result vector display.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {2-5}
Post.Template.Create(strName="Vector_Template", strComment="Attach Vector Template")
template = Post.Template.AttachVector(strName="Vector_Template", 
                                    postDataVizOptVector=POST_DATA_VIZ_OPT_VECTOR(
                                        dRatioModel=0.05, 
                                        dRatioScreen=0.05))
JPT.Debugger(template)
```
