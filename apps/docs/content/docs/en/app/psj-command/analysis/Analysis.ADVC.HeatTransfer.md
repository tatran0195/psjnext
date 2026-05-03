---
title: "Analysis.ADVC.HeatTransfer()"
description: "Create and export the ADVC (*.adx) file for the Heat Transfer analysis"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Analysis > ADVC > Heat Transfer"
---

## Description

Create and export the ADVC (\*.adx) file for the Heat Transfer analysis.

## Syntax

```psj
Analysis.ADVC.HeatTransfer(...)
```

## Inputs

### `strName` @type(String) @required

- The job name of ADVC analysis. This name would be the name of analysis job in Assembly Tree and the name of ADX file after exported.

### `strDescription` @type(String) @default("")

- The description for ADVC analysis job. The description would write in ADX file, where contents will be written below ModelInfo.

### `crlProcessSequence` @type(List\[Cursor]) @default(\[])

- The ADVC process sequences. This argument controls the Process solution type and its setting information depended on solution type.

### `crlElemLocationGroup` @type(List\[Cursor]) @default(\[])

- The element locations. The model contains Element group such as 3D Element, 2D Element, 1D Element to use this argument.

### `crlNodeLocationGroup` @type(List\[Cursor]) @default(\[])

- The node locations. The model contains Node group to use this argument.

### `bWriteGroup` @type(Boolean) @default(False)

- Whether to write group which output a selected group of Faces, Elements, Nodes as Surface Segment, Element Set and Node set respectively.
  - I&#x66;_&#x62;WriteGroup=True_, the ADX file would contained group information such as Part, Face, Element(3D, 2D, 1D), Node,...

### `crEdit` @type(Cursor) @default(None)

- The existing ADVC job in Assembly Tree. If this argument is no&#x74;_&#x4E;one_, the specified ADVC job will be modified. Otherwise, a new job will be created.

### `bResultReference` @type(Boolean) @default(False)

- Whether to use the settings of Result Reference.
  - I&#x66;_&#x62;ResultReference=True_, the settings of Result Reference arguments will be valid to use.

### `iSeparateFile` @type(Integer) @default(0)

- The method to separate file. This option allows to separate information into many exported ADX files by the specified type.
  - I&#x66;_&#x69;SeparateFile=0_, this option would export only 1 ADX file contains all information of all bodies/parts in the model (ModelInfo, Unit, Geometry, LBCs, Process Sequence,...).
  - I&#x66;_&#x69;SeparateFile=1_, this option would export 2 ADX files, which the first ADX file has same name as analysis Job will contain general information (such as ModelInfo, Unit, LBCs, Job name, Process Sequence, other settings of ADVC Structure analysis). When the last one ADX file which has suffix name "\_model", contains Geometry information (such as Node, Part, Element,...).
  - I&#x66;_&#x69;SeparateFile=2_, this option would export ADX files, which each body/part in model would be written individually Geometry information, Group in model would be written in another file, while other information would be written in the ADX file has same name as analysis Job.
  - I&#x66;_&#x69;SeparateFile=3_, this option would export ADX file that write information of selected part/body. If selection does not have at least a specific body/part, Jupiter would write all bodies/part (same option a&#x73;_&#x69;SeparateFile=0_).
  - I&#x66;_&#x69;SeparateFile=4_, this option would export 1 ADX file contains LBCs information of the chosen LBCs.

### `bExportRelatedAllLBCs` @type(Boolean) @default(False)

- Whether to export all related Load Boundary Condition. This argument is to be used whe&#x6E;_&#x69;SeparateFile=3_.
  - I&#x66;_&#x54;rue_, this option would export ADX file contains related information to LBCs such as Contact, Connection RBE, Bolt Pretension,...

### `bUseEntityName` @type(Boolean) @default(False)

- Whether to use entity name in exported file or not.
  - I&#x66;_&#x54;rue_, this option would export ADX file that write Entity name to Geometry information such as Part, Face,...
  - I&#x66;_&#x46;alse_, this option would export ADX file without writing Entities name to Geometry information.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The list of targets. The target could be Part or LBCs item.

### `iLoadType` @type(Integer) @default(1)

- The load type used for analysis.
  - I&#x66;_&#x69;LoadType=0_: Load Case, which is a group of specific Loads, BCs applies on the model. The model could apply many Load Cases which may have same setting of LBCs. Exporting ADX file would write all Load Cases.
  - I&#x66;_&#x69;LoadType=1_: Load, which will export ADX file stores all Loads, BCs as a 1 Load case only.

### `bSameOutputOnAllProcess` @type(Boolean) @default(True)

- Whether to use the same output request for all processes.
  - I&#x66;_&#x54;rue_, set same output request (Displacement, Stress, Strain,...) for all defined processes.
  - I&#x66;_&#x46;alse_, set output request which will base on user's desired result for each process.

### `bDeleteFloatingNode` @type(Boolean) @default(True)

- Whether to delete floating nodes or not.
  - I&#x66;_&#x54;rue_, the exported ADX file would not write the floating nodes information.
  - I&#x66;_&#x46;alse_, the exported ADX file would write the floating nodes information.

### `bBC` @type(Boolean) @default(True)

- Whether to separate boundary condition. This argument is to be used whe&#x6E;_&#x69;SeparateFile=3_.
  - I&#x66;_&#x54;rue_, the exported ADX file would write LBCs information.

### `bCheckBCDuplicate` @type(Boolean) @default(False)

- Whether to check if duplicate the boundary conditions.
  - I&#x66;_&#x54;rue_, to check LBCs duplication when export ADX file.

### `bAutoAssignDummyProp` @type(Boolean) @default(False)

- Whether to automatically assign dummy property for dummy entities. This argument is to be used when the model has that unassigned property.
  - I&#x66;_&#x54;rue_, the model would be exported with dummy property for the Part that does not have property. The others Part (which already assigned property) will export with its property setting.
  - I&#x66;_&#x46;alse_, the model will export ADX file in case of the model has all property in all Parts, but if there is one Part that does not have property in the model, this option will not export file.

### `crDummyPropMaterial` @type(Cursor) @default(None)

- The dummy property material for automatically assigning dummy property when export ADX file.

### `bReferenceRestartData` @type(Boolean) @default(False)

- Whether to use the Reference Restart Data.
  - I&#x66;_&#x54;rue_, the settings of Reference Restart Data arguments will be valid to use.
  - I&#x66;_&#x46;alse_, the settings of Reference Restart Data arguments will be ignored even though User has set value or not.

### `strReferenceRestartDataPath` @type(String) @default("")

- The path of Reference Restart Data.

### `iNumberProcesses` @type(Integer) @default(DFLT\_INT)

- The number of processes for Reference Restart Data.

### `iNumberSteps` @type(Integer) @default(DFLT\_INT)

- The number steps of Reference Restart Data.

### `iCoordinateType` @type(Integer) @default(0)

- The coordinate type of Reference Restart Data.
  - I&#x66;_&#x69;CoordinateType=0_: Initial type
  - I&#x66;_&#x69;CoordinateType=1_: Deformation type

### `iUpdateContactSearch` @type(Integer) @default(1)

- Whether to update contact search for Reference Restart Data.
  - I&#x66;_&#x69;UpdateContactSearch=0_: No
  - I&#x66;_&#x69;UpdateContactSearch=1_: Yes

### `listLoadNodeContact` @type(List\[LOAD\_NODE\_CONTACT]) @default(\[])

- The list of load node contacts.

### `iHeatConvection` @type(Integer) @default(1)

- The Heat Convection type. There are 2 types of Heat Convection:
  - I&#x66;_&#x69;HeatConvection=0_: Direct
  - I&#x66;_&#x69;HeatConvection=1_: Indirect

### `strPath` @type(String) @default("")

- The exporting path for ADX file.

### `iNumType` @type(Integer) @default(0)

- The numeric format type. This argument would allow numeric setting type of adx file.
  - I&#x66;_&#x69;NumType=0_: Real Type - The numerical values in real number format (e.g 123.456).
  - I&#x66;_&#x69;NumType=1_: Power Type - The numerical values in exponential/scientific format (e.g 1.234E-005).

### `iUiWidth` @type(Integer) @default(10)

- The limitation number of digits before the point of the number. This option allows to control number digits of value in exported ADX file.

### `iUiPrecision` @type(Integer) @default(1)

- The limitation number of digits after the point of the number. This option allows to control number digits of value in exported ADX file.

### `bExportGeometryID` @type(Boolean) @default(False)

- Whether to write geometry ID number.

### `bSeparatePartInfoFile` @type(Boolean) @default(False)

- Whether to separate Part Information Files.

### `strADVCTemplateFilePath` @type(String) @default("")

- The path of ADVC Template File.

### `bOutputDefinition` @type(Boolean) @default(True)

- To be enable/disable the option that sets the output request.

## Return Code

A _Cursor_ specifying the created jobs.

## Sample Code

```psj {30-38}
Geometry.Part.Cube(iPartColor=5619133)
Meshing.SolidMeshing(crlParts=[Part(1)],
                     bTet10=True,
                     dGradingFactor=1.05,
                     dStretchLimit=0.1,
                     iSpeedVsQual=1,
                     iRegion=1,
                     bSafeMode=False,
                     iParallel=12,
                     bInternalMeshOnly=False,
                     iPartColor=65280)

Properties.Material.Add("Concrete",
                        [Density([(DENSITY, 2.3e-09)]),
                        Elastic([(YOUNGS_MODULUS, 30000.0),
                                 (POISSONS_RATIO, 0.18)])])

Properties.Solid(crlTargets=[Part(1)],
                 strName="Solid Property 1",
                 iPropertyColor=12275404,
                 crMaterial=Material(1),
                 iCordM=-2,
                 dDynaRemeshVal1=DFLT_DBL,
                 dDynaRemeshVal2=DFLT_DBL,
                 dDispHG=DFLT_DBL,
                 iFLG=-1)

Analysis.ADVC.MakeProcess.SteadyState(strName="Process_0")

creating_status = Analysis.ADVC.HeatTransfer(strPath="D:/Job_1.adx",
                                             strName="Job_1",
                                             crlProcessSequence=[ADVCProcessSSH(1)],
                                             crlTargets=[Part(1)],
                                             bAutoAssignDummyProp=True,
                                             crDummyPropMaterial=Material(1),
                                             listLoadNodeContact=[],
                                             iUiPrecision=6,
                                             bExportGeometryID=True)

JPT.Debugger(creating_status)
```
