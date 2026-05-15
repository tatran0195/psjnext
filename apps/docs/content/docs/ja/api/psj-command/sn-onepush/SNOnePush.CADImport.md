---
title: "SNOnePush.CADImport()"
description: "import CAD model"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "SNOnePush > CADImport"
---

## Description

Import CAD model

## Syntax

```psj
SNOnePush.CADImport(dDsurfaceplaneTolerance, dDsurfaceplaneAngle, dMaxFacetWidth, bBnxMultipart, dChordHeightTolerance, dAngleToleranceDegree, iConvertIsolatedCurve, iIigesFixedcurevepreference, iIigesAutostitch, dDigesStitchtolerance, iIcatiaConvertnotshowedelement, iIcatiaConvertnotshowedinstance, iIcatiaConvertaxis, iIstepCreateseam, dDstepPointtolerance, iIacisHealacisbeforeversion, iIjtConvertgeometrytype, iIjtConvertgeneralpart, iIjtConvertaxis, iIjtConvertcenterline, dDcreoChordheighttolerance, dDcreoAngletolerancedegree, strAbsCreoPath, iTransType, iFileType, strFilePath, bRenameDuplicateName, strCSVFilePath)
```

## Inputs

<!-- @since:5.0.1 @required -->
### dDsurfaceplaneTolerance

- Specify the dsurfaceplane tolerance.

<!-- @since:5.0.1 @required -->
### dDsurfaceplaneAngle

- Specify the dsurfaceplane angle.

<!-- @since:5.0.1 @required -->
### dMaxFacetWidth

- Specify the maximum facet width.

<!-- @since:5.0.1 @required -->
### bBnxMultipart

- Specify the bnx multipart.

<!-- @since:5.0.1 @required -->
### dChordHeightTolerance

- Specify the chord height tolerance.

<!-- @since:5.0.1 @required -->
### dAngleToleranceDegree

- Specify the angle tolerance degree.

<!-- @since:5.0.1 @required -->
### iConvertIsolatedCurve

- Specify the convert isolated curve.

<!-- @since:5.0.1 @required -->
### iIigesFixedcurevepreference

- Specify the iiges fixed cureve preference.

<!-- @since:5.0.1 @required -->
### iIigesAutostitch

- Specify the iiges auto stitch.

<!-- @since:5.0.1 @required -->
### dDigesStitchtolerance

- Specify the diges stitch tolerance.

<!-- @since:5.0.1 @required -->
### iIcatiaConvertnotshowedelement

- Specify the icatia convert not showed element.

<!-- @since:5.0.1 @required -->
### iIcatiaConvertnotshowedinstance

- Specify the icatia convert not showed instance.

<!-- @since:5.0.1 @required -->
### iIcatiaConvertaxis

- Specify the icatia convert axis.

<!-- @since:5.0.1 @required -->
### iIstepCreateseam

- Specify the istep create seam.

<!-- @since:5.0.1 @required -->
### dDstepPointtolerance

- Specify the dstep point tolerance.

<!-- @since:5.0.1 @required -->
### iIacisHealacisbeforeversion

- Specify the iacis heal acis before version.

<!-- @since:5.0.1 @required -->
### iIjtConvertgeometrytype

- Specify the ijt convert geometry type.

<!-- @since:5.0.1 @required -->
### iIjtConvertgeneralpart

- Specify the ijt convert general part.

<!-- @since:5.0.1 @required -->
### iIjtConvertaxis

- Specify the ijt convert axis.

<!-- @since:5.0.1 @required -->
### iIjtConvertcenterline

- Specify the ijt convert center line.

<!-- @since:5.0.1 @required -->
### dDcreoChordheighttolerance

- Specify the dcreo chord height tolerance.

<!-- @since:5.0.1 @required -->
### dDcreoAngletolerancedegree

- Specify the dcreo angle tolerance degree.

<!-- @since:5.0.1 @required -->
### strAbsCreoPath

- Specify the abs creo path.

<!-- @since:5.0.1 @required -->
### iTransType

- Specify the trans type.

<!-- @since:5.0.1 @required -->
### iFileType

- Specify the file type.

<!-- @since:5.0.1 @required -->
### strFilePath

- Specify the file path.

<!-- @since:5.0.1 @required -->
### bRenameDuplicateName

- Specify the rename duplicate name.

<!-- @since:5.0.1 @required -->
### strCSVFilePath

- Specify the CSV file path.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
SNOnePush.CADImport(dDsurfaceplaneTolerance, dDsurfaceplaneAngle, dMaxFacetWidth, bBnxMultipart, dChordHeightTolerance, dAngleToleranceDegree, iConvertIsolatedCurve, iIigesFixedcurevepreference, iIigesAutostitch, dDigesStitchtolerance, iIcatiaConvertnotshowedelement, iIcatiaConvertnotshowedinstance, iIcatiaConvertaxis, iIstepCreateseam, dDstepPointtolerance, iIacisHealacisbeforeversion, iIjtConvertgeometrytype, iIjtConvertgeneralpart, iIjtConvertaxis, iIjtConvertcenterline, dDcreoChordheighttolerance, dDcreoAngletolerancedegree, strAbsCreoPath, iTransType, iFileType, strFilePath, bRenameDuplicateName, strCSVFilePath)
```
