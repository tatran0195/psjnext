---
title: "Post.Template.AttachDiagram()"
description: "Attach the current diagram settings to the specified template"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > Template > AttachDiagram"
macro _link: "[AttachTemplateDiagram](../../macro/post/AttachTemplateDiagram)"
---

## Description

Attach the current diagram settings to the specified template.

## Syntax

```psj
Post.Template.AttachDiagram(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### strName

- Specify the name of template, which will attach the diagram settings.
- The default value is "NewTemplate".

<!-- @since:5.1.0 @optional -->
### postDataVizOptDiagram

- Specify all settings of the diagram display.
- The default value is [POST\_DATA\_VIZ\_OPT\_DIAGRAM](../../data-type/psj-command/parameter-types/POST _DATA _VIZ _OPT _DIAGRAM).

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {2-5}
Post.Template.Create(strName="Diagram _Template", strComment="Attach Diagram Template")
template = Post.Template.AttachDiagram(strName="Diagram _Template", 
                                    postDataVizOptDiagram=POST _DATA _VIZ _OPT _DIAGRAM(
                                        dRatioModel=0.05, 
                                        dRatioScreen=0.05))
JPT.Debugger(template)
```
