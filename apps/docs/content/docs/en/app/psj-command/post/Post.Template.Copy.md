---
title: "Post.Template.Copy()"
description: "Create a copy of the specified template"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > Template > Copy"
macro_link: "[CopyTemplate](../../macro/post/CopyTemplate)"
---

## Description

Create a copy of the specified template.

## Syntax

```psj
Post.Template.Copy(...)
```

## Inputs

### `strCurrentTemplate` @type(String) @required

- The name of the template that will create a copy.

### `strNewTemplate` @type(String) @required

- The name of the copied template.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {12}
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
Post.Template.Copy(strCurrentTemplate="Template_1", strNewTemplate="Template_2")
```
