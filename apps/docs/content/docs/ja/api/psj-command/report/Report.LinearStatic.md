---
title: "Report.LinearStatic()"
description: "Search for parts (components) whose displayed static analysis results are outside the result thresholds set for parts and materials, captures images and automatically pastes them into Microsoft Office PowerPoint"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Report > LinearStatic"
macro _link: "[CmdGeneralReportLinearStatic](../../macro/report/CmdGeneralReportLinearStatic)"
---

## Description

Search for parts (components) whose displayed static analysis results are outside the result thresholds set for parts and materials, captures images and automatically pastes them into Microsoft Office PowerPoint.

## Syntax

```psj
Report.LinearStatic(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### iCalculateValue

- Specify the evaluation value.
  - 0: Mises.
  - 1: Maximum principal.
  - 2: Minimum principal.
  - 3: Displacement.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iEvaluationValue

- Specify the evaluation expression.
  - O: A/B for A is evaluation value and B is standard value.
  - 1: B/A for A is evaluation value and B is standard value.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### listPartInformation

- Specify the attribute of components.
- The default value is GENERAL\_REPORT\_LINEAR\_STATIC\_DATA().

<!-- @since:5.1.0 @optional -->
### bUseCurrentView

- Specify whether to use the current view as perspective.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### bExportPPT

- Specify whether to export the result image to PowerPoint.
- The default value is _True_.

<!-- @since:5.1.0 @optional -->
### bExportImage

- Specify whether to save the result image to file.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### strImagePath

- Specify the path of image file to be saved in the specified format.
- The default value is "".

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {7-44}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101 _solid.op2"
Home.ImportResults.Nastran(strPath= samplePath, dFaceAngle=60.16, dEdgeAngle=60.16, bReadLoadAndConstraint=True, 
                            bReadConnection=True, bCreateResultsAtMidNode=True)

# Make Linear Static report
reportLinearStatic = Report.LinearStatic(iCalculateValue=1, 
                                        listPartInformation=[
                                        General _Report _LinearStatic _Data(
                                            strPartName="All", 
                                            strPropName="-", 
                                            strMatName="-", 
                                            dValue=0.000000), 
                                        General _Report _LinearStatic _Data(
                                            strPartName="Part - PSOLID (1)", 
                                            strPropName="PSOLID (1)", 
                                            strMatName="MAT (1)", 
                                            dValue=0.000000), 
                                        General _Report _LinearStatic _Data(
                                            strPartName="Part - PSOLID (2)", 
                                            strPropName="PSOLID (2)", 
                                            strMatName="MAT (1)", 
                                            dValue=0.000000), 
                                        General _Report _LinearStatic _Data(
                                            strPartName="Part - PSOLID (3)", 
                                            strPropName="PSOLID (3)", 
                                            strMatName="MAT (1)", 
                                            dValue=0.000000), 
                                        General _Report _LinearStatic _Data(
                                            strPartName="Part - PSOLID (4)", 
                                            strPropName="PSOLID (4)", 
                                            strMatName="MAT (1)", 
                                            dValue=0.000000), 
                                        General _Report _LinearStatic _Data(
                                            strPartName="Part - PSOLID (5)", 
                                            strPropName="PSOLID (5)", 
                                            strMatName="MAT (1)", 
                                            dValue=0.000000), 
                                        General _Report _LinearStatic _Data(
                                            strPartName="Part - PSOLID (6)", 
                                            strPropName="PSOLID (6)", 
                                            strMatName="MAT (1)", 
                                            dValue=0.000000)], 
                                            bExportPPT=True)
JPT.Debugger(reportLinearStatic)
```
