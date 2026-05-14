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

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iResultInOnePage`

- The number of result images to paste on one page of the PowerPoint file. The option is 1, 2, 4 and 6.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bUseCurrentView`

- Whether to use the current view as perspective.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bExportPPT`

- Whether to export the result image to PowerPoint.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bExportImage`

- Whether to save the result image to file.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dStartFrequency`

- The start frequency. Any frequency less than this value will be ignored.

<!-- @since:5.1.0 @type:Double @optional @default:100.0 -->
### `dEndFrequency`

- The end frequency. Any frequency greater than this value will be ignored.

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strImagePath`

- The path of image file to be saved in the specified format.

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
