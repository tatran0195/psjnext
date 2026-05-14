---
title: "Post.Template.Create()"
description: "Create a new template"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > Template > Create"
macro _link: "[CreateTemplate](../../macro/post/CreateTemplate)"
---

## Description

Create a new template.

## Syntax

```psj
Post.Template.Create(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @optional @default:"NewTemplate" -->
### `strName`

- The template name.

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strComment`

- The comments for the created template.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {6-11}
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
```
