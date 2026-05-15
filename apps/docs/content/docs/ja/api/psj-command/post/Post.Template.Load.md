---
title: "Post.Template.Load()"
description: "Load the specified template in the template list to the current screen"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > Template > Load"
macro _link: "[LoadTemplate](../../macro/post/LoadTemplate)"
---

## Description

Load the specified template in the template list to the current screen.

## Syntax

```psj
Post.Template.Load(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### strName

- Specify the name of template will be loaded.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {14}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103 _solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Create new Template
Post.Template.Create(strName="Template _1", strComment="")
Post.Template.AttachViewPoint(
    strName="Template _1", 
    postDataVizOptViewPoint=POST _DATA _VIZ _OPT _VIEWPOINT(
        dlCenter=[0.016, 0.005, 0.0025], 
        dScaleFactor=0.0349344))

# Load template
loadTemplate = Post.Template.Load(strName="Template _1")
JPT.Debugger(loadTemplate)
```
