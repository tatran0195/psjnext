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

<!-- @since:5.1.0 @optional -->
### strName

- Specify the name of template, which will attach the vector settings.
- The default value is "NewTemplate".

<!-- @since:5.1.0 @optional -->
### postDataVizOptVector

- Specify all settings of the result vector display.
- The default value is [POST\_DATA\_VIZ\_OPT\_VECTOR](../../data-type/psj-command/parameter-types/POST _DATA _VIZ _OPT _VECTOR).

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
