---
title: "Post.Template.Export()"
description: "Export the current template settings to a .xml file"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > Template > Export"
macro_link: "[ExportTemplate](../../macro/post/ExportTemplate)"
---

## Description

Export the current template settings to a .xml file.

## Syntax

```psj
Post.Template.Export(...)
```

## Inputs

### `strPath` @type(String) @required

- The path of \*.xml file to be exported.

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

# Export template
exportTemplate = Post.Template.Export(strPath="C:/temp/Template_1.xml")
JPT.Debugger(exportTemplate)
```
