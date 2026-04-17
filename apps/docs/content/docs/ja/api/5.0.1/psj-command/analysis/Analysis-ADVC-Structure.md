---
id: Analysis.ADVC.Structure
title: Analysis.ADVC.Structure()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create and export the ADVC (*.adx) file for the Structure analysis
---

## Description

Create and export the ADVC (\*.adx) file for the Structure analysis.

## Syntax

```psj
Analysis.ADVC.Structure(...)
```

Ribbon: <menuselection>Analysis &#187; ADVC &#187; Structure</menuselection>

## Inputs

### `strName`

- A _String_ specifying the job name of ADVC analysis. This name would be the name of analysis job in Assembly Tree and the name of the ADX file after exported.
- The default value is "".

### `strDescription`

- A _String_ specifying the description for ADVC analysis job. The description would write in the ADX file, where contents will be written below ModelInfo.
- The default value is "".

[comment]: # 'This argument `iEJobType` is removed and not available in V5.0.1 or higher version'

<!-- ### `iEJobType`

- An _Integer_ specifying the job type of ADVC analysis. ADVC supports 2 types of analysis.
  - If _iEJobType=0_: The analysis job is Structure analysis
  - If _iEJobType=1_: The analysis job is Heat Transfer analysis
- The default value is 0. -->

### `crlProcessSequence`

- A _List of Cursor_ specifying the list of ADVC process sequence. This argument controls the Process solution type and its setting information depended on solution type.
- The default value is [].

### `crlElemLocationGroup`

- A _List of Cursor_ specifying the list of element location. The model contains element group such as 3D Element, 2D Element, 1D Element to use this argument.
- The default value is [].

### `crlNodeLocationGroup`

- A _List of Cursor_ specifying the list of node location. The model contains node group to use this argument.
- The default value is [].

### `bWriteGroup`

- A _Boolean_ specifying to be enable/disable the write group option which output a selected group of faces, elements, nodes as Surface Segment, Element Set and Node set respectively.
    - If _True_, ADX file would contained group information such as Part, Face, Element(3D,2D,1D), Node,...
    - If _False_, ADX won't write group information.
- The default value is _False_.

### `crEdit`

- A _Cursor_ specifying an existing ADVC job in Assembly Tree to modify it. If this parameter is used, the specified ADVC job will be modified. If it is left _None_, a new ADVC job will be created.
- The default value is _None_.

### `bResultReference`

- A _Boolean_ specifying to be enable/disable the Result Reference option is defined or not.
    - If _True_, this option will allow to active settings of Result Reference. The settings of Result Reference arguments will be valid to use.
    - If _False_, this option will be disable settings of Result Reference. In this case, the settings of Result Reference arguments will be ignored even though User has set value or not.
- The default value is _False_.

### `iSeparateFile`

- An _Integer_ specifying the separate file type. This option allows to separate information into many exported ADX files by selected type.
    - If _iSeparateFile=0_: None, this option would export only 1 ADX file contains all information of all bodies/parts in the model (ModelInfo, Unit, Geometry, LBCs, Process Sequence,...)
    - If _iSeparateFile=1_: By Model, this option would export 2 ADX files, which the first ADX file has same name as analysis Job will contain general information (such as ModelInfo, Unit, LBCs, Job name, Process Sequence, other settings of ADVC Structure analysis).
      When the last one ADX file which has suffix name "\_model", contains Geometry information (such as Node, Part, Element,...)
    - If _iSeparateFile=2_: By Body, this option would export ADX files, which each body/part in model would be written individually Geometry information, Group in model would be written in another file, while other information would be written in the ADX file has same name as analysis Job.
    - If _iSeparateFile=3_: By Selected Body, this option would export ADX file that write information of selected part/body. If selection does not have at least a specific body/part, Jupiter would write all bodies/part (same option as None).
    - If _iSeparateFile=4_: By Selected LBCs, this option would export 1 ADX file contains LBCs information of the chosen LBCs.
- The default value is 0.

### `bExportRelatedAllLBCs`

- A _Boolean_ specifying to be enable/disable the option that export all related Load Boundary Condition. This option could be used when _iSeparateFile=3_(By Selected Body), if not, this setting is not activated for both _True_ or _False_.
    - If _True_, this option would export the ADX file contains related information to LBCs such as Contact, Connection RBE, Bolt Pretension,...
    - If _False_, this option won't export related information to LBCs such as Contact, Connection RBE, Bolt Pretension,...
- The default value is _False_.

### `bUseEntityName`

- A _Boolean_ specifying to be enable/disable the option that use entity name in exported file or not.
    - If _True_, this option would export the ADX file that write Entity name(Name of the Part/Entity) to Geometry information such as Part, Face,...
    - If _False_, this option would export the ADX file without writing Entities name to Geometry information.
- The default value is _False_.

### `bMatrixSolverParam`

- A _Boolean_ specifying to be enable/disable the option that the Matrix Solver Parameter is defined ot not.
    - If _True_, this option will allow to active settings of Matrix Solver Parameter. The settings of Matrix Solver Parameter arguments will be valid to use.
    - If _False_, this option will be disable settings of Matrix Solver Parameter. In this case, the settings of Matrix Solver Parameter arguments will be ignored even though User has set value or not.
- The default value is _False_.

### `iPreconditionType`

- An _Integer_ specifying the precondition type.
    - If _iPreconditionType=0_: Scaling
    - If _iPreconditionType=1_: CGCG
    - If _iPreconditionType=2_: CGCG2
    - If _iPreconditionType=3_: CGCG2_Diag
    - If _iPreconditionType=4_: CGCG2-SOR
- The default value is 0.

### `iMatrixStructure`

- An _Integer_ specifying the matrix structure type.
    - If _iMatrixStructure=0_: Symmetry
    - If _iMatrixStructure=1_: Asymmetry
- The default value is 0.

### `crlTargets`

- A _List of Cursor_ specifying the list of targets. The target could be Part or LBCs item.
- The default value is [].

### `iLoadType`

- An _Integer_ specifying the load type uses for analysis.
    - If _iLoadType=0_: Load Case, which is a group of specific Loads, BCs applies on model. The model could apply many Load Cases which may have same setting of LBCs. Exporting ADX file would write all Load Cases.
    - If _iLoadType=1_: Load, which will export the ADX file stores all Loads, BCs as a 1 Load case only.
- The default value is 1.

### `bSameOutputOnAllProcess`

- A _Boolean_ specifying to be enable/disable the same output request for all processes.
    - If _True_, this option would set same output request (Displacement, Stress, Strain,...) for all defined processes.
    - If _False_, this option would set output request which will base on user's desired result for each process.
- The default value is _True_.

### `bDeleteFloatingNode`

- A _Boolean_ specifying to be enable/disable the option that would delete floating node or not.
    - If _True_, this option would export an ADX file without writing floating nodes information.
    - If _False_, this option would export an ADX file with floating nodes information.
- The default value is _True_.

### `bBC`

- A _Boolean_ specifying to be enable/disable the option that would separate boundary condition. This option could be used when _iSeparateFile=3_ (By Selected Body), if not, this setting is not activated for both _True_ or _False_.
    - If _True_, this option would export an ADX file would write LBCs information.
    - If _False_, this option won't export an ADX file would write LBCs information.
- The default value is _True_.

### `bCheckBCDuplicate`

- A _Boolean_ specifying to be enable/disable checking whether boundary conditions are duplicated or not.
    - If _True_, this option checks LBCs duplication when export the ADX file.
    - If _False_, this option won't check LBCs duplication when export the ADX file.
- The default value is _False_.

### `bAutoAssignDummyProp`

- A _Boolean_ specifying to be enable/disable automatically assign dummy property option. This option used when model that has not assign property yet. If the model already has property
    - If _True_, the model would be exported with dummy property for the Part that does not have property. The others Part (which already assigned property) will export with its property setting.
    - If _False_, the model will export ADX file in case of the model has all property in all Parts, but if there is one Part that does not have property in the model, this option will not export file.
- The default value is _False_.

### `crDummyPropMaterial`

- A _Cursor_ specifying the dummy property material for automatically assigning dummy property when export the ADX file.
- The default value is _None_.

### `bReferenceRestartData`

- A _Boolean_ specifying to be enable/disable the Reference Restart Data is defined or not.
    - If _True_, this option will allow to active settings of Reference Restart Data. The settings of Reference Restart Data arguments will be valid to use.
    - If _False_, this option will be disable settings of Reference Restart Data. In this case, the settings of Reference Restart Data arguments will be ignored even though User has set value or not.
- The default value is _False_.

### `strReferenceRestartDataPath`

- A _String_ specifying the path of Reference Restart Data.
- The default value is "".

### `iReferenceRestartDataProcessNum`

- An _Integer_ specifying the number of process for Reference Restart Data.
- The default value is DFLT_INT.

### `iReferenceRestartDataStepNum`

- An _Integer_ specifying the number of Reference Restart Data step.
- The default value is DFLT_INT.

### `iReferenceRestartDataCoordType`

- An _Integer_ specifying the coordinate type of Reference Restart Data.
    - If _iReferenceRestartDataCoordType=0_: Initial type
    - If _iReferenceRestartDataCoordType=1_: Deformation type
- The default value is 0.

### `iReferenceRestartDataUpdateContactSearch`

- An _Integer_ specifying the update contact search for Reference Restart Data.
    - If _iReferenceRestartDataUpdateContactSearch=0_: No
    - If _iReferenceRestartDataUpdateContactSearch=1_: Yes
- The default value is 1.

### `listLoadNodeContact`

- A _LOAD_NODE_CONTACT List_ specifying the list of load node contact.
- The default value is [].

[comment]: # 'This argument `iHeatConvection` is removed and not available in V5.0.1 or higher version'

<!-- ### `iHeatConvection`

- An _Integer_ specifying the heat convection.
- The default value is 1. -->

### `bCreateProcessForBoltFixedLength`

- A _Boolean_ specifying the option that creates process for bolt fixed length.
    - If _True_, this option will set the "Bolt Fixed Length" given in the initial process to hold in the next process.
    - If _False_, this option will won't take the "Bolt Fixed Length" setting in the initial process to apply on the next process.
- This setting uses the character string "BoltLoadFixedLength".
- The default value is _False_.

### `strPath`

- A _String_ specifying the exporting path for the ADX file.
- This is a required input.

### `iNumType`

- An _Integer_ specifying the numeric format type. This argument would allow numeric setting type of the ADX file.
    - If _iNumType=0_: Real Type - The numerical values in real number format (123.456).
    - If _iNumType=1_: Power Type - The numerical values in exponential/scientific format (1.234E-005).
- The default value is 0.

### `iUiWidth`

- An _Integer_ specifying the limitation number of digits before the point of the number. This option allows to control number digits of value in the exported ADX file.
- The default value is 10.

### `iUiPrecision`

- An _Integer_ specifying the limitation number of digits after the point of the number. This option allows to control number digits of value in the exported ADX file.
- The default value is 1.

### `bExportGeometryID`

- A _Boolean_ specifying to be enable/disable the write geometry ID number.
- The default value is _False_.

### `bSeparatePartInfoFile`

- A _Boolean_ specifying to be enable/disable the option that separate Part Information Files.
- The default value is _False_.

### `strADVCTemplateFilePath`

- A _String_ specifying the path of Template File.
- The default value is "".

### `bOutputDefinition`

- A _Boolean_ specifying to be enable/disable the option that sets the output request.
- The default value is _True_.

## Return Code

A _Cursor_ specifying the created jobs.
