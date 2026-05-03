---
title: "Post.Template.Load()"
description: "Load the specified template in the template list to the current screen"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > Template > Load"
macro_link: "[LoadTemplate](../../macro/post/LoadTemplate)"
---

## Description

Load the specified template in the template list to the current screen.

## Syntax

```psj
Post.Template.Load(...)
```

## Inputs

### `strName` @type(String) @required

- The name of template will be loaded.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {14}
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

# Load template
loadTemplate = Post.Template.Load(strName="Template_1")
JPT.Debugger(loadTemplate)
```
