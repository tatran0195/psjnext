---
title: "Analysis.ADVC.HeatTransfer()"
description: "Create and export the ADVC (*.adx) file for the Heat Transfer analysis"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > ADVC > Heat Transfer"
---

## Description

Create and export the ADVC (\*.adx) file for the Heat Transfer analysis.

## Syntax

```psj
Analysis.ADVC.HeatTransfer(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The job name of ADVC analysis. This name would be the name of analysis job in Assembly Tree and the name of ADX file after exported.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strDescription`

- The description for ADVC analysis job. The description would write in ADX file, where contents will be written below ModelInfo.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlProcessSequence`

- The ADVC process sequences. This argument controls the Process solution type and its setting information depended on solution type.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlElemLocationGroup`

- The element locations. The model contains Element group such as 3D Element, 2D Element, 1D Element to use this argument.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlNodeLocationGroup`

- The node locations. The model contains Node group to use this argument.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bWriteGroup`

- Whether to write group which output a selected group of Faces, Elements, Nodes as Surface Segment, Element Set and Node set respectively.
  - If _bWriteGroup=True_, the ADX file would contained group information such as Part, Face, Element(3D, 2D, 1D), Node,...

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The existing ADVC job in Assembly Tree. If this argument is not _None_, the specified ADVC job will be modified. Otherwise, a new job will be created.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bResultReference`

- Whether to use the settings of Result Reference.
  - If _bResultReference=True_, the settings of Result Reference arguments will be valid to use.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSeparateFile`

- The method to separate file. This option allows to separate information into many exported ADX files by the specified type.
  - If _iSeparateFile=0_, this option would export only 1 ADX file contains all information of all bodies/parts in the model (ModelInfo, Unit, Geometry, LBCs, Process Sequence,...).
  - If _iSeparateFile=1_, this option would export 2 ADX files, which the first ADX file has same name as analysis Job will contain general information (such as ModelInfo, Unit, LBCs, Job name, Process Sequence, other settings of ADVC Structure analysis). When the last one ADX file which has suffix name "\_model", contains Geometry information (such as Node, Part, Element,...).
  - If _iSeparateFile=2_, this option would export ADX files, which each body/part in model would be written individually Geometry information, Group in model would be written in another file, while other information would be written in the ADX file has same name as analysis Job.
  - If _iSeparateFile=3_, this option would export ADX file that write information of selected part/body. If selection does not have at least a specific body/part, Jupiter would write all bodies/part (same option as _iSeparateFile=0_).
  - If _iSeparateFile=4_, this option would export 1 ADX file contains LBCs information of the chosen LBCs.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bExportRelatedAllLBCs`

- Whether to export all related Load Boundary Condition. This argument is to be used when _iSeparateFile=3_.
  - If _True_, this option would export ADX file contains related information to LBCs such as Contact, Connection RBE, Bolt Pretension,...

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bUseEntityName`

- Whether to use entity name in exported file or not.
  - If _True_, this option would export ADX file that write Entity name to Geometry information such as Part, Face,...
  - If _False_, this option would export ADX file without writing Entities name to Geometry information.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The list of targets. The target could be Part or LBCs item.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iLoadType`

- The load type used for analysis.
  - If _iLoadType=0_: Load Case, which is a group of specific Loads, BCs applies on the model. The model could apply many Load Cases which may have same setting of LBCs. Exporting ADX file would write all Load Cases.
  - If _iLoadType=1_: Load, which will export ADX file stores all Loads, BCs as a 1 Load case only.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bSameOutputOnAllProcess`

- Whether to use the same output request for all processes.
  - If _True_, set same output request (Displacement, Stress, Strain,...) for all defined processes.
  - If _False_, set output request which will base on user's desired result for each process.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bDeleteFloatingNode`

- Whether to delete floating nodes or not.
  - If _True_, the exported ADX file would not write the floating nodes information.
  - If _False_, the exported ADX file would write the floating nodes information.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bBC`

- Whether to separate boundary condition. This argument is to be used when _iSeparateFile=3_.
  - If _True_, the exported ADX file would write LBCs information.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bCheckBCDuplicate`

- Whether to check if duplicate the boundary conditions.
  - If _True_, to check LBCs duplication when export ADX file.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bAutoAssignDummyProp`

- Whether to automatically assign dummy property for dummy entities. This argument is to be used when the model has that unassigned property.
  - If _True_, the model would be exported with dummy property for the Part that does not have property. The others Part (which already assigned property) will export with its property setting.
  - If _False_, the model will export ADX file in case of the model has all property in all Parts, but if there is one Part that does not have property in the model, this option will not export file.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crDummyPropMaterial`

- The dummy property material for automatically assigning dummy property when export ADX file.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bReferenceRestartData`

- Whether to use the Reference Restart Data.
  - If _True_, the settings of Reference Restart Data arguments will be valid to use.
  - If _False_, the settings of Reference Restart Data arguments will be ignored even though User has set value or not.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strReferenceRestartDataPath`

- The path of Reference Restart Data.

<!-- @since:5.0.1 @type:Integer @optional @default:DFLT _INT -->
### `iNumberProcesses`

- The number of processes for Reference Restart Data.

<!-- @since:5.0.1 @type:Integer @optional @default:DFLT _INT -->
### `iNumberSteps`

- The number steps of Reference Restart Data.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iCoordinateType`

- The coordinate type of Reference Restart Data.
  - If _iCoordinateType=0_: Initial type
  - If _iCoordinateType=1_: Deformation type

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iUpdateContactSearch`

- Whether to update contact search for Reference Restart Data.
  - If _iUpdateContactSearch=0_: No
  - If _iUpdateContactSearch=1_: Yes

<!-- @since:5.0.1 @type:List[LOAD _NODE _CONTACT] @optional @default:[] -->
### `listLoadNodeContact`

- The list of load node contacts.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iHeatConvection`

- The Heat Convection type. There are 2 types of Heat Convection:
  - If _iHeatConvection=0_: Direct
  - If _iHeatConvection=1_: Indirect

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strPath`

- The exporting path for ADX file.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iNumType`

- The numeric format type. This argument would allow numeric setting type of adx file.
  - If _iNumType=0_: Real Type - The numerical values in real number format (e.g 123.456).
  - If _iNumType=1_: Power Type - The numerical values in exponential/scientific format (e.g 1.234E-005).

<!-- @since:5.0.1 @type:Integer @optional @default:10 -->
### `iUiWidth`

- The limitation number of digits before the point of the number. This option allows to control number digits of value in exported ADX file.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iUiPrecision`

- The limitation number of digits after the point of the number. This option allows to control number digits of value in exported ADX file.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bExportGeometryID`

- Whether to write geometry ID number.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bSeparatePartInfoFile`

- Whether to separate Part Information Files.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strADVCTemplateFilePath`

- The path of ADVC Template File.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bOutputDefinition`

- The to be enable/disable the option that sets the output request.

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
                        Elastic([(YOUNGS _MODULUS, 30000.0),
                                 (POISSONS _RATIO, 0.18)])])

Properties.Solid(crlTargets=[Part(1)],
                 strName="Solid Property 1",
                 iPropertyColor=12275404,
                 crMaterial=Material(1),
                 iCordM=-2,
                 dDynaRemeshVal1=DFLT _DBL,
                 dDynaRemeshVal2=DFLT _DBL,
                 dDispHG=DFLT _DBL,
                 iFLG=-1)

Analysis.ADVC.MakeProcess.SteadyState(strName="Process _0")

creating _status = Analysis.ADVC.HeatTransfer(strPath="D:/Job _1.adx",
                                             strName="Job _1",
                                             crlProcessSequence=[ADVCProcessSSH(1)],
                                             crlTargets=[Part(1)],
                                             bAutoAssignDummyProp=True,
                                             crDummyPropMaterial=Material(1),
                                             listLoadNodeContact=[],
                                             iUiPrecision=6,
                                             bExportGeometryID=True)

JPT.Debugger(creating _status)
```
