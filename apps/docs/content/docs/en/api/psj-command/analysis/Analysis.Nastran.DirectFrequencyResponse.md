---
title: "Analysis.Nastran.DirectFrequencyResponse()"
description: "Export the input file for Nastran Direct Frequency Response Analysis (SOL 108)"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Analysis > Nastran > DirectFrequencyResponse"
macro _link: ""
---

## Description

Export the input file for Nastran Direct Frequency Response Analysis (SOL 108).

## Syntax

```psj
Analysis.Nastran.DirectFrequencyResponse(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @optional @default:"Job _1" -->
### `strName`

- The job name of Nastran analysis

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strDescription`

- The description of Nastran analysis job.

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The list of target parts.

<!-- @since:5.1.0 @type:NASTRAN _ANALYSIS @optional @default:NASTRAN _ANALYSIS -->
### `nastranAnalysis`

- The Nastran analysis input parameter.

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strPath`

- The export path for bdf file.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iModelCheckAnswer`

- The model checking option.
  - 0: disable model checking option used for seeking dummy property.
  - 1: enable model checking option used for seeking dummy property.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iDeleteSlaveNodesAnswer`

- The deleting slave nodes option.
  - 0: disable the deleting slave nodes checking option.
  - 1: enable the deleting slave nodes checking option.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bOutputXYPlots`

- Whether to output X–Y plot.

<!-- @since:5.1.0 @type:Integer @optional @default:-1 -->
### `iOutputValueSet`

- The group node.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iOutputDOFType`

- The degrees of freedom to output for each result.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iXYPlotDisplacementType`

- The displacement output destination.
  - 0: None
  - 264: XYPunch - Output the XY table to a punch file (\*.pch).
  - 520: XYPlot - Outputs the XY table to a plot output file (\*.plt).
  - 776: XYPunch\&XYPlot - Outputs the XY table to both a punch file and a plot output file.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iXYPlotVelocityType`

- The velocity output destination.
  - 0: None
  - 264: XYPunch - Output the XY table to a punch file (\*.pch).
  - 520: XYPlot - Outputs the XY table to a plot output file (\*.plt).
  - 776: XYPunch\&XYPlot - Outputs the XY table to both a punch file and a plot output file.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iXYPlotAccelerationType`

- The acceleration output destination.
  - 0: None
  - 264: XYPunch - Output the XY table to a punch file (\*.pch).
  - 520: XYPlot - Outputs the XY table to a plot output file (\*.plt).
  - 776: XYPunch\&XYPlot - Outputs the XY table to both a punch file and a plot output file.

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strXTitle`

- The X-axis title.

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strYTitle`

- The Y-axis title.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bDummyPropAutoAssign`

- Whether to assign dummy properties to parts without assigned properties automatically.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bOutputGeomIDofDummyProp`

- Whether to output entity IDs (Face, Edge, Part).

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iDummyPropMaterialID`

- The material ID which using for dummy property assignment.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing Nastran job.
  - If this parameter is used, the specified job will be modified.
  - If it is left _None_, a new job will be created.

## Return Code

A _Cursor_ specifying the newly created or the modified Nastran job.

## Sample Code

```psj {72-116}
Geometry.Part.Cube(iPartColor=6409934)
Meshing.AdjustCircleVertex(crlParts=[Part(1)], bInModeSurfaceMesh=True)
Meshing.SetMeshAttribute(
    crlParts=[Part(1)], 
    surfaceMesh=SURFACE _MESH(
        dGeomAngle=0.7853981634, 
        iPerformanceMode=1, 
        dAutoMergeTinyFacesAngle=0.5235987756, 
        bGeomApprox=True))
Meshing.SurfaceMeshing(
    crlParts=[Part(1)], 
    surfaceMesh=SURFACE _MESH(
        dGeomAngle=0.7853981634, 
        iPerformanceMode=1, 
        dAutoMergeTinyFacesAngle=0.5235987756, 
        bGeomApprox=True), 
    iThreadNum=16)
Properties.Material.Add(
        strMaterialName="Structural _Steel", 
        dictMaterialProperty={
            'Density': {'density': {'DENSITY': [7850.000000000001]}}, 
            'Elastic': {'elastic': {'YOUNGS _MODULUS': [200000000000.0], 
            'POISSONS _RATIO': [0.3]}}, 
            'Expansion': {'expansion': {'ALPHA': [1.2e-05]}}, 
            'Conductivity': {'conductivity': {'CONDUCTIVITY': [59.0]}}, 
            'SpecificHeat': {'specificHeat': {'SPECIFIC _HEAT': [461.0]}}}, 
        iMaterialID=5, 
        iMaterialColor=10264731)
BoundaryConditions.FixedConstraint(strName="Constraint _1", crlTargets=[Node(491, 489, 490, 492)])
BoundaryConditions.Force.General(
    strName="Force _1", 
    forceLBC=FORCE _LBC(vecForce=[DFLT _DBL, DFLT _DBL, 55.555556]), 
    crlTargets=[Node(495)])
BoundaryConditions.Force.General(
    strName="Force _2", 
    forceLBC=FORCE _LBC(vecForce=[DFLT _DBL, DFLT _DBL, 88.555556]), 
    crlTargets=[Node(494)])
MeshEdit.CreateNode.Offset(vecOffset=[0.0, 0.0, -0.001], crlNodes=[Node(491)])
Connections.SpringsDampers.Spring.OneToOne.sameDoFs(
    iMethod=17, 
    strName="Spring _1", 
    crlMasterTargets=[Node(491)], 
    crlSlaveTargets=[Node(515)], 
    iSpringType=2, d
    Tolerance=DFLT _DBL, 
    posTStiffness=[1000000, 1.7976931e+308, 1.7976931e+308], 
    posRStiffness=[1.7976931e+308, 1.7976931e+308, 1.7976931e+308])
Connections.MassElements(
    strName="Mass _1", 
    crlTargets=[Node(513)], 
    dMass=36779.0, 
    iDof=6, 
    bDesigner=False, 
    dInertia0=DFLT _DBL, 
    dInertia1=DFLT _DBL, 
    dInertia2=DFLT _DBL, 
    dInertia3=DFLT _DBL, 
    dInertia4=DFLT _DBL, 
    dInertia5=DFLT _DBL)
BoundaryConditions.FieldData(
    strName="FieldData1", 
    iType=4, 
    ilSheet=[10, 2, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0])
Properties.Shell(
    crlTargets=[Part(1)], 
    strName="ShellProperty _1", 
    iPropertyColor=16131973, 
    crMatMembrane=Material(5), 
    crMatBend=Material(5), 
    crMatShear=Material(5), 
    dThickness=0.0003)
ret = Analysis.Nastran.DirectFrequencyResponse(
    strName="SOL108", 
    strDescription="SOL108", 
    nastranAnalysis=NASTRAN _ANALYSIS(
        iSolverType=1, 
        iGridFormatType=1, 
        bDeleteFloatingNodes=True, 
        bContinuanceMarker=True, 
        dEpsilon=DFLT _DBL, 
        iMaxNumOfIter=DFLT _INT, 
        iMemory=2, 
        iNcpu=1, 
        iSolNo=108, 
        nastranFrequency=NASTRAN _FREQUENCY(iTableId=1), 
        nastranOutputRequest=NASTRAN _OUTPUT _REQUEST(
            iValueSdisplacement=DFLT _INT, 
            iValueAcceleration=DFLT _INT, 
            iValueVelocity=DFLT _INT, 
            iTypeDisplacement=9, 
            iTypeStress=9, 
            iTypeStrain=0), 
        nastranCaseControl=NASTRAN _CASE _CONTROL(
            strTitle="NAS _SUPPORT _CARD _FOR _SOL108"), 
        nastranSettings=NASTRAN _SETTINGS(
            iAUTOSPC=1, 
            strGRDPNT="0", 
            strK6ROT="1.000000", 
            iBAILOUT=-1, 
            iMEFFMASS=1, 
            dCUTOFF _VALUE=5.5), 
        nastranSubcase=[NASTRAN _SUBCASE(
            iId=1, 
            strTitle="Subcase1", 
            iSubcaseIdForDload=DFLT _INT, 
            iSubcaseIdForSpc=DFLT _INT)]), 
    bDummyPropAutoAssign=True, 
    iDummyPropMaterialID=5, 
    strPath="C:/temp/SOL108.bdf", 
    bOutputXYPlots=True, 
    iOutputDOFType=4, 
    iXYPlotDisplacementType=264, 
    iXYPlotVelocityType=264, 
    iXYPlotAccelerationType=264, 
    strYTitle="ACCE PSD", 
    bOutputGeomIDofDummyProp=True)
print(ret)
```
