---
title: "Post.Template.AttachCrossSection()"
description: "Attach the current cross section settings to the specified template"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > Template > AttachCrossSection"
macro_link: "[AttachTemplateCrossSection](../../macro/post/AttachTemplateCrossSection)"
---

## Description

Attach the current cross section settings to the specified template.

## Syntax

```psj
Post.Template.AttachCrossSection(...)
```

## Inputs

### `strName` @type(String) @default("NewTemplate")

- The name of template, which will attach the cross section settings.

### `postDataVizOptCrossSection` @type(POST\_DATA\_VIZ\_OPT\_SECTION) @default(POST\_DATA\_VIZ\_OPT\_SECTION)

- All settings of the cross section display.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {2-9}
Post.Template.Create(strName="Cross Section", strComment="Attach Cross Section Template")
template = Post.Template.AttachCrossSection(strName="Cross Section", 
                                        postDataVizOptCrossSection=POST_DATA_VIZ_OPT_CROSS_SECTION(
                                            bCapping=False, 
                                            bCuttingEdge=True, 
                                            bSectionElem=True, 
                                            bMeshLine=True, 
                                            dlTranslationMatrix=[1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.016, 0.005, 0.0025, 1.0], 
                                            dlPosition=[0.016, 0.005, 0.0025]))
JPT.Debugger(template)
```
