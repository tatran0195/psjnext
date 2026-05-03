---
title: "Report.LinearStatic()"
description: "Search for parts (components) whose displayed static analysis results are outside the result thresholds set for parts and materials, captures images and automatically pastes them into Microsoft Office PowerPoint"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Report > LinearStatic"
macro_link: "[CmdGeneralReportLinearStatic](../../macro/report/CmdGeneralReportLinearStatic)"
---

## Description

Search for parts (components) whose displayed static analysis results are outside the result thresholds set for parts and materials, captures images and automatically pastes them into Microsoft Office PowerPoint.

## Syntax

```psj
Report.LinearStatic(...)
```

## Inputs

### `iCalculateValue` @type(Integer) @default(0)

- The evaluation value.
  - 0: Mises.
  - 1: Maximum principal.
  - 2: Minimum principal.
  - 3: Displacement.

### `iEvaluationValue` @type(Integer) @default(0)

- The evaluation expression.
  - O: A/B for A is evaluation value and B is standard value.
  - 1: B/A for A is evaluation value and B is standard value.

### `listPartInformation` @type(List\[GENERAL\_REPORT\_LINEAR\_STATIC\_DATA]) @default(GENERAL\_REPORT\_LINEAR\_STATIC\_DATA())

- The attribute of components.

### `bUseCurrentView` @type(Boolean) @default(False)

- Whether to use the current view as perspective.

### `bExportPPT` @type(Boolean) @default(True)

- Whether to export the result image to PowerPoint.

### `bExportImage` @type(Boolean) @default(False)

- Whether to save the result image to file.

### `strImagePath` @type(String) @default("")

- The path of image file to be saved in the specified format.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {7-44}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
Home.ImportResults.Nastran(strPath= samplePath, dFaceAngle=60.16, dEdgeAngle=60.16, bReadLoadAndConstraint=True, 
                            bReadConnection=True, bCreateResultsAtMidNode=True)

# Make Linear Static report
reportLinearStatic = Report.LinearStatic(iCalculateValue=1, 
                                        listPartInformation=[
                                        General_Report_LinearStatic_Data(
                                            strPartName="All", 
                                            strPropName="-", 
                                            strMatName="-", 
                                            dValue=0.000000), 
                                        General_Report_LinearStatic_Data(
                                            strPartName="Part - PSOLID (1)", 
                                            strPropName="PSOLID (1)", 
                                            strMatName="MAT (1)", 
                                            dValue=0.000000), 
                                        General_Report_LinearStatic_Data(
                                            strPartName="Part - PSOLID (2)", 
                                            strPropName="PSOLID (2)", 
                                            strMatName="MAT (1)", 
                                            dValue=0.000000), 
                                        General_Report_LinearStatic_Data(
                                            strPartName="Part - PSOLID (3)", 
                                            strPropName="PSOLID (3)", 
                                            strMatName="MAT (1)", 
                                            dValue=0.000000), 
                                        General_Report_LinearStatic_Data(
                                            strPartName="Part - PSOLID (4)", 
                                            strPropName="PSOLID (4)", 
                                            strMatName="MAT (1)", 
                                            dValue=0.000000), 
                                        General_Report_LinearStatic_Data(
                                            strPartName="Part - PSOLID (5)", 
                                            strPropName="PSOLID (5)", 
                                            strMatName="MAT (1)", 
                                            dValue=0.000000), 
                                        General_Report_LinearStatic_Data(
                                            strPartName="Part - PSOLID (6)", 
                                            strPropName="PSOLID (6)", 
                                            strMatName="MAT (1)", 
                                            dValue=0.000000)], 
                                            bExportPPT=True)
JPT.Debugger(reportLinearStatic)
```
