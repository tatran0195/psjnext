---
title: "Report.Modal()"
description: "Capture the image of the displayed modal result of the eigenvalue analysis at each frequency within the specified range, and automatically paste it into Microsoft Office PowerPoint"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Report > Modal"
macro _link: "[CmdGeneralReportModal](../../macro/report/CmdGeneralReportModal)"
---

## Description

Capture the image of the displayed modal result of the eigenvalue analysis at each frequency within the specified range, and automatically paste it into Microsoft Office PowerPoint.

## Syntax

```psj
Report.Modal(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### iResultInOnePage

- Specify the number of result images to paste on one page of the PowerPoint file. The option is 1, 2, 4 and 6.
- The default value is 1.

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
### dStartFrequency

- Specify the start frequency. Any frequency less than this value will be ignored.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dEndFrequency

- Specify the end frequency. Any frequency greater than this value will be ignored.
- The default value is 100.0.

<!-- @since:5.1.0 @optional -->
### strImagePath

- Specify the path of image file to be saved in the specified format.
- The default value is "".

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {6}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103 _solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60, dEdgeAngle=60)

# Make Modal report
reportModal = Report.Modal(iResultInOnePage=2, dStartFrequency=10000.0, dEndFrequency=100000.0)
JPT.Debugger(reportModal)
```
