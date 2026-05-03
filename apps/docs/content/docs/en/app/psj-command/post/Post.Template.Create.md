---
title: "Post.Template.Create()"
description: "Create a new template"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > Template > Create"
macro_link: "[CreateTemplate](../../macro/post/CreateTemplate)"
---

## Description

Create a new template.

## Syntax

```psj
Post.Template.Create(...)
```

## Inputs

### `strName` @type(String) @default("NewTemplate")

- The template name.

### `strComment` @type(String) @default("")

- Comments for the created template.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {6-11}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Create new Template
Post.Template.Create(strName="Template_1", strComment="")
Post.Template.AttachViewPoint(
    strName="Template_1", 
    postDataVizOptViewPoint=POST_DATA_VIZ_OPT_VIEWPOINT(
        dlCenter=[0.016, 0.005, 0.0025], 
        dScaleFactor=0.0349344))
```
