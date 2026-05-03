---
title: "Analysis.Ansys.NormalModes()"
description: "Export the Ansys Normal Modes Structural solver file"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Analysis > Ansys > NormalModes"
---

## Description

Export the Ansys Normal Modes Structural solver file.

## Syntax

```psj
Analysis.Ansys.NormalModes(...)
```

## Inputs

### `strJobName` @type(String) @required

- The job name of Ansys analysis.

### `strAnsysJobName` @type(String) @default("Job1")

- The the name of Ansys Normal Modes Structural analysis.

### `strAnsysJobdescription` @type(String) @default("")

- The description for new Ansys analysis.

### `bRunAPDL` @type(Boolean) @default(False)

- Enable/disalbe the option that running Ansys Parametric Design Language (APDL).

### `bWriteResultDB` @type(Boolean) @default(False)

- Enable/disalbe the option that write result database.

### `dEndFreq` @type(Double) @default(DFLT\_DBL)

- The end frequency number.

### `dStartFreq` @type(Double) @default(DFLT\_DBL)

- The start frequency number.

### `iLoadCaseId` @type(Integer) @default(0)

- The load case identify number .

### `ansysAnalysisModal` @type(\[MODAL]./../../data-type/psj-command/parameter-types/(MODAL)) @default(MODAL)

- The Ansys Analysis - Modal Structural input parameter.

### `strAnsysVersion` @type(String) @default("")

- The Ansys Version information.

### `strCommandLineOption` @type(String) @default("")

- The Command Line Option information.

### `bOutputSOLVE` @type(Boolean) @default(False)

- Enable/disalbe SOLVE command write out.

### `crEdit` @type(Cursor) @default(None)

- The editing ansys job.

### `strFileName` @type(String) @default("")

- The exporting path for .dat file.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {3}
Geometry.Part.Cube()

Analysis.Ansys.NormalModes("Job1", iLoadCaseId=1, strFileName="C:/Job1.dat")
```
