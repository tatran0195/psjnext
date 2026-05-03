---
title: "Post.Template.Update()"
description: "Update a specified template"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > Template > Update"
macro_link: "[UpdateTemplate](../../macro/post/UpdateTemplate)"
---

## Description

Update a specified template.

## Syntax

```psj
Post.Template.Update(...)
```

## Inputs

### `strName` @type(String) @required

- The template name to be updated.

### `strComment` @type(String) @default("")

- The comment when updating the template.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {14-19}
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

# Updated the created template
Post.Template.Update(strName="Template_1", strComment="Update View Point ")
Post.Template.AttachViewPoint(
    strName="Template_1", 
    postDataVizOptViewPoint=POST_DATA_VIZ_OPT_VIEWPOINT(
        dlCenter=[0.003, 0.005, 0.001], 
        dScaleFactor=0.00753137))
```
