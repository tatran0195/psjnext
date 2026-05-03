---
title: "Post.Template.Delete()"
description: "Delete a specified template"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > Template > Delete"
macro_link: "[DeleteTemplate](../../macro/post/DeleteTemplate)"
---

## Description

Delete a specified template.

## Syntax

```psj
Post.Template.Delete(...)
```

## Inputs

### `strName` @type(String) @required

- The name of template will be deleted.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {13}
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
Post.Template.Delete(strName="Template_2")
```
