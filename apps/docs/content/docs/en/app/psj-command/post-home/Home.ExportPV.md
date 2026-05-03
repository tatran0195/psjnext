---
title: "Home.ExportPV()"
description: "Output the results to PV files according to three types of elements, or materials, or properties"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > ExportPV"
macro_link: "[Export_Post_Viewer_File](../../macro/home/Export_Post_Viewer_File)"
---

## Description

Output the results to PV files according to three types of elements, or materials, or properties.

## Syntax

```psj
Home.ExportPV(...)
```

## Inputs

### `iGroupType` @type(Integer) @default(0)

- The type of output group.
  - 0: None
  - 1: Specify the element created in the group
  - 2: Specify the material created in the group
  - 3: Specify the property created in the group

### `strFileName` @type(String) @default("")

- The file path to be exported.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {26}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16) 
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(
                    postResultKey=PostResultKey(
                        iAnalysisType=1, 
                        iResultSet=1, 
                        iTimeStep=1, 
                        strResultName="Displacement", 
                        strResultCompName="Translational", 
                        iResultPos=1), 
                    postDataOp=PostDataOp(
                        iResultLocation=1, 
                        iOptionCoord=1))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                        iAnalysisType=1, 
                        iResultSet=1, 
                        iTimeStep=1, 
                        strResultName="Displacement", 
                        strResultCompName="Translational"))
Tools.Group.CreateGroup(strGroupName="Element3DGroup", crlTargets=[ROElem(479, 477, 480, 478)])

# Export PV
exportFile = Home.ExportPV(iGroupType=1, strFileName="C:/temp/ExportPV.tsv")
JPT.Debugger(exportFile)
```
