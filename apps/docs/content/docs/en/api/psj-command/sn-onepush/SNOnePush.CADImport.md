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

<!-- @since:5.0.1 @type:Double @required -->
### `dDsurfaceplaneTolerance`

- The dsurfaceplane tolerance.

<!-- @since:5.0.1 @type:Double @required -->
### `dDsurfaceplaneAngle`

- The dsurfaceplane angle.

<!-- @since:5.0.1 @type:Double @required -->
### `dMaxFacetWidth`

- The maximum facet width.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bBnxMultipart`

- The bnx multipart.

<!-- @since:5.0.1 @type:Double @required -->
### `dChordHeightTolerance`

- The chord height tolerance.

<!-- @since:5.0.1 @type:Double @required -->
### `dAngleToleranceDegree`

- The angle tolerance degree.

<!-- @since:5.0.1 @type:Integer @required -->
### `iConvertIsolatedCurve`

- The convert isolated curve.

<!-- @since:5.0.1 @type:Integer @required -->
### `iIigesFixedcurevepreference`

- The iiges fixed cureve preference.

<!-- @since:5.0.1 @type:Integer @required -->
### `iIigesAutostitch`

- The iiges auto stitch.

<!-- @since:5.0.1 @type:Double @required -->
### `dDigesStitchtolerance`

- The diges stitch tolerance.

<!-- @since:5.0.1 @type:Integer @required -->
### `iIcatiaConvertnotshowedelement`

- The icatia convert not showed element.

<!-- @since:5.0.1 @type:Integer @required -->
### `iIcatiaConvertnotshowedinstance`

- The icatia convert not showed instance.

<!-- @since:5.0.1 @type:Integer @required -->
### `iIcatiaConvertaxis`

- The icatia convert axis.

<!-- @since:5.0.1 @type:Integer @required -->
### `iIstepCreateseam`

- The istep create seam.

<!-- @since:5.0.1 @type:Double @required -->
### `dDstepPointtolerance`

- The dstep point tolerance.

<!-- @since:5.0.1 @type:Integer @required -->
### `iIacisHealacisbeforeversion`

- The iacis heal acis before version.

<!-- @since:5.0.1 @type:Integer @required -->
### `iIjtConvertgeometrytype`

- The ijt convert geometry type.

<!-- @since:5.0.1 @type:Integer @required -->
### `iIjtConvertgeneralpart`

- The ijt convert general part.

<!-- @since:5.0.1 @type:Integer @required -->
### `iIjtConvertaxis`

- The ijt convert axis.

<!-- @since:5.0.1 @type:Integer @required -->
### `iIjtConvertcenterline`

- The ijt convert center line.

<!-- @since:5.0.1 @type:Double @required -->
### `dDcreoChordheighttolerance`

- The dcreo chord height tolerance.

<!-- @since:5.0.1 @type:Double @required -->
### `dDcreoAngletolerancedegree`

- The dcreo angle tolerance degree.

<!-- @since:5.0.1 @type:String @required -->
### `strAbsCreoPath`

- The abs creo path.

<!-- @since:5.0.1 @type:Integer @required -->
### `iTransType`

- The trans type.

<!-- @since:5.0.1 @type:Integer @required -->
### `iFileType`

- The file type.

<!-- @since:5.0.1 @type:String @required -->
### `strFilePath`

- The file path.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bRenameDuplicateName`

- The rename duplicate name.

<!-- @since:5.0.1 @type:String @required -->
### `strCSVFilePath`

- The CSV file path.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
SNOnePush.CADImport(dDsurfaceplaneTolerance, dDsurfaceplaneAngle, dMaxFacetWidth, bBnxMultipart, dChordHeightTolerance, dAngleToleranceDegree, iConvertIsolatedCurve, iIigesFixedcurevepreference, iIigesAutostitch, dDigesStitchtolerance, iIcatiaConvertnotshowedelement, iIcatiaConvertnotshowedinstance, iIcatiaConvertaxis, iIstepCreateseam, dDstepPointtolerance, iIacisHealacisbeforeversion, iIjtConvertgeometrytype, iIjtConvertgeneralpart, iIjtConvertaxis, iIjtConvertcenterline, dDcreoChordheighttolerance, dDcreoAngletolerancedegree, strAbsCreoPath, iTransType, iFileType, strFilePath, bRenameDuplicateName, strCSVFilePath)
```
