---
title: "SNOnePush.CADImport()"
description: "import CAD model"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "SNOnePush > CADImport"
---

## Description

Import CAD model

## Syntax

```psj
SNOnePush.CADImport(dDsurfaceplaneTolerance, dDsurfaceplaneAngle, dMaxFacetWidth, bBnxMultipart, dChordHeightTolerance, dAngleToleranceDegree, iConvertIsolatedCurve, iIigesFixedcurevepreference, iIigesAutostitch, dDigesStitchtolerance, iIcatiaConvertnotshowedelement, iIcatiaConvertnotshowedinstance, iIcatiaConvertaxis, iIstepCreateseam, dDstepPointtolerance, iIacisHealacisbeforeversion, iIjtConvertgeometrytype, iIjtConvertgeneralpart, iIjtConvertaxis, iIjtConvertcenterline, dDcreoChordheighttolerance, dDcreoAngletolerancedegree, strAbsCreoPath, iTransType, iFileType, strFilePath, bRenameDuplicateName, strCSVFilePath)
```

## Inputs

### `dDsurfaceplaneTolerance` @type(Double) @required

- The dsurfaceplane tolerance.

### `dDsurfaceplaneAngle` @type(Double) @required

- The dsurfaceplane angle.

### `dMaxFacetWidth` @type(Double) @required

- The maximum facet width.

### `bBnxMultipart` @type(Boolean) @required

- The bnx multipart.

### `dChordHeightTolerance` @type(Double) @required

- The chord height tolerance.

### `dAngleToleranceDegree` @type(Double) @required

- The angle tolerance degree.

### `iConvertIsolatedCurve` @type(Integer) @required

- The convert isolated curve.

### `iIigesFixedcurevepreference` @type(Integer) @required

- The iiges fixed cureve preference.

### `iIigesAutostitch` @type(Integer) @required

- The iiges auto stitch.

### `dDigesStitchtolerance` @type(Double) @required

- The diges stitch tolerance.

### `iIcatiaConvertnotshowedelement` @type(Integer) @required

- The icatia convert not showed element.

### `iIcatiaConvertnotshowedinstance` @type(Integer) @required

- The icatia convert not showed instance.

### `iIcatiaConvertaxis` @type(Integer) @required

- The icatia convert axis.

### `iIstepCreateseam` @type(Integer) @required

- The istep create seam.

### `dDstepPointtolerance` @type(Double) @required

- The dstep point tolerance.

### `iIacisHealacisbeforeversion` @type(Integer) @required

- The iacis heal acis before version.

### `iIjtConvertgeometrytype` @type(Integer) @required

- The ijt convert geometry type.

### `iIjtConvertgeneralpart` @type(Integer) @required

- The ijt convert general part.

### `iIjtConvertaxis` @type(Integer) @required

- The ijt convert axis.

### `iIjtConvertcenterline` @type(Integer) @required

- The ijt convert center line.

### `dDcreoChordheighttolerance` @type(Double) @required

- The dcreo chord height tolerance.

### `dDcreoAngletolerancedegree` @type(Double) @required

- The dcreo angle tolerance degree.

### `strAbsCreoPath` @type(String) @required

- The abs creo path.

### `iTransType` @type(Integer) @required

- The trans type.

### `iFileType` @type(Integer) @required

- The file type.

### `strFilePath` @type(String) @required

- The file path.

### `bRenameDuplicateName` @type(Boolean) @required

- The rename duplicate name.

### `strCSVFilePath` @type(String) @required

- The CSV file path.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
SNOnePush.CADImport(dDsurfaceplaneTolerance, dDsurfaceplaneAngle, dMaxFacetWidth, bBnxMultipart, dChordHeightTolerance, dAngleToleranceDegree, iConvertIsolatedCurve, iIigesFixedcurevepreference, iIigesAutostitch, dDigesStitchtolerance, iIcatiaConvertnotshowedelement, iIcatiaConvertnotshowedinstance, iIcatiaConvertaxis, iIstepCreateseam, dDstepPointtolerance, iIacisHealacisbeforeversion, iIjtConvertgeometrytype, iIjtConvertgeneralpart, iIjtConvertaxis, iIjtConvertcenterline, dDcreoChordheighttolerance, dDcreoAngletolerancedegree, strAbsCreoPath, iTransType, iFileType, strFilePath, bRenameDuplicateName, strCSVFilePath)
```
