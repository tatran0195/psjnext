---
title: "Post.Template.AttachDiagram()"
description: "Attach the current diagram settings to the specified template"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > Template > AttachDiagram"
macro_link: "[AttachTemplateDiagram](../../macro/post/AttachTemplateDiagram)"
---

## Description

Attach the current diagram settings to the specified template.

## Syntax

```psj
Post.Template.AttachDiagram(...)
```

## Inputs

### `strName` @type(String) @default("NewTemplate")

- The name of template, which will attach the diagram settings.

### `postDataVizOptDiagram` @type(POST\_DATA\_VIZ\_OPT\_DIAGRAM) @default(POST\_DATA\_VIZ\_OPT\_DIAGRAM)

- All settings of the diagram display.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {2-5}
Post.Template.Create(strName="Diagram_Template", strComment="Attach Diagram Template")
template = Post.Template.AttachDiagram(strName="Diagram_Template", 
                                    postDataVizOptDiagram=POST_DATA_VIZ_OPT_DIAGRAM(
                                        dRatioModel=0.05, 
                                        dRatioScreen=0.05))
JPT.Debugger(template)
```
