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

<!-- @since:5.1.0 @type:String @optional @default:"NewTemplate" -->
### `strName`

- The name of template, which will attach the diagram settings.

<!-- @since:5.1.0 @type:POST _DATA _VIZ _OPT _DIAGRAM @optional @default:POST _DATA _VIZ _OPT _DIAGRAM -->
### `postDataVizOptDiagram`

- The all settings of the diagram display.

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
