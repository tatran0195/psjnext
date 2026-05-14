---
title: "Post.Template.Import()"
description: "Import the contents of the saved template settings (*.xml) into the template list"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > Template > Import"
macro _link: "[ImportTemplate](../../macro/post/ImportTemplate)"
---

## Description

Import the contents of the saved template settings (\*.xml) into the template list.

## Syntax

```psj
Post.Template.Import(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `strPath`

- The path of \*.xml file will be imported.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {16}
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
Post.Template.Export(strPath="C:/temp/Template _1.xml")
Post.Template.Delete(strName="Template _1")

# Import template
importTemplate = Post.Template.Import(strPath="C:/temp/Template _1.xml")
JPT.Debugger(importTemplate)
```
