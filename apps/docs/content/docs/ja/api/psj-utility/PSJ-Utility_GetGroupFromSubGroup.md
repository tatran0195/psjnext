---
title: "JPT.GetGroupFromSubGroup()"
description: "Get all the information of all the existing groups under the specified group's name"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get the _List of Groups_ under the specified group's name.

## Syntax

```psj
JPT.GetGroupFromSubGroup(groupName)
```

## Inputs

<!-- @since:5.0.1 @required -->
### groupName

- Specify the name of the existing group using for getting all the information of the group inside.

## Return Code

A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects specifying groups which are under the specified group's name.

## Sample Code

```psj {242,245}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0],
                   strName="Cube _2",
                   iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0],
                   strName="Cube _3",
                   iPartColor=13259210)
Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0],
                   strName="Cube _4",
                   iPartColor=7697908)
Geometry.Part.Cube(dlOrigin=[0.04, 0.0, 0.0],
                   strName="Cube _5",
                   iPartColor=7463537)
Geometry.Part.Cube(dlOrigin=[0.05, 0.0, 0.0],
                   strName="Cube _6",
                   iPartColor=7434735)
Geometry.Part.Cube(dlOrigin=[0.06, 0.0, 0.0],
                   strName="Cube _7",
                   iPartColor=14903267)
Geometry.Part.Cube(dlOrigin=[0.07, 0.0, 0.0],
                   strName="Cube _8",
                   iPartColor=15658599)
JPT.ViewFitToModel()

Meshing.SetMeshAttribute(crlParts=[Part(5, 6, 7, 8)],
                         surfaceMesh=SURFACE _MESH(dGeomAngle=0.7853981634,
                                                  iPerformanceMode=1,
                                                  dAutoMergeTinyFacesAngle=0.5235987756,
                                                  bOutputQuadMesh=True,
                                                  bGeomApprox=True,
                                                  iNextEntityOffsetId=0))
Meshing.SurfaceMeshing(crlParts=[Part(5, 6, 7, 8)],
                       surfaceMesh=SURFACE _MESH(dGeomAngle=0.7853981634,
                                                iPerformanceMode=1,
                                                dAutoMergeTinyFacesAngle=0.5235987756,
                                                bOutputQuadMesh=True,
                                                bGeomApprox=True,
                                                iNextEntityOffsetId=0),
                                                iThreadNum=12)
MeshEdit.SurfaceMesh(crlParts=[Part(2, 4, 8, 6)])
Meshing.SolidMeshing(crlParts=[Part(8, 4, 7, 3)],
                     dGradingFactor=1.05,
                     dStretchLimit=0.1,
                     iSpeedVsQual=1,
                     iRegion=1,
                     bSafeMode=False,
                     iParallel=12,
                     bInternalMeshOnly=False,
                     iPartColor=65280)
Meshing.SolidMeshing(crlParts=[Part(4)],
                     bTet10=True,
                     dGradingFactor=1.05,
                     dStretchLimit=0.1,
                     iSpeedVsQual=1,
                     iRegion=1,
                     bSafeMode=False,
                     iParallel=12,
                     bInternalMeshOnly=False,
                     iPartColor=65280)

del _faces = [208, 182, 178, 204, 206, 177, 203, 179, 205, 180]
extrude _faces = [207, 181]

Geometry.DeleteEntity.Face(crlFaces=[Face(*del _faces)])

HexModeling.Linear(crlFaces=[Face(*extrude _faces)],
                   dLength=0.01,
                   iLayer=2,
                   vecSweepDirection=[0.0,
                                      0.0,
                                      1.0],
                   iLinearMethod=4)

MeshEdit.SolidMesh(crlParts=[Part(8)])

Properties.Material.Add(strMaterialName="Copper _Alloy",
                        listMaterialProperty=[Density([(DENSITY,
                                                        8.3e-09)]),
                                              Elastic([(YOUNGS _MODULUS,
                                                        110000.0),
                                                       (POISSONS _RATIO,
                                                        0.34)])])
Properties.Material.Add(strMaterialName="Magnesium _Alloy",
                        listMaterialProperty=[Density([(DENSITY,
                                                        1.8e-09)]),
                                              Elastic([(YOUNGS _MODULUS,
                                                        45000.0),
                                                       (POISSONS _RATIO,
                                                        0.35)])])
Properties.Material.Add(strMaterialName="Concrete",
                        listMaterialProperty=[Density([(DENSITY,
                                                        2.3e-09)]),
                                              Elastic([(YOUNGS _MODULUS,
                                                        30000.0),
                                                       (POISSONS _RATIO,
                                                        0.18)])])
Properties.Material.Add(strMaterialName="Polyethylene",
                        listMaterialProperty=[Density([(DENSITY,
                                                        9.5e-10)]),
                                              Elastic([(YOUNGS _MODULUS,
                                                        1100.0),
                                                       (POISSONS _RATIO,
                                                        0.42)])])
Properties.Material.Add(strMaterialName="Structural _Steel",
                        listMaterialProperty=[Density([(DENSITY,
                                                        7.85e-09)]),
                                              Elastic([(YOUNGS _MODULUS,
                                                        200000.0),
                                                       (POISSONS _RATIO,
                                                        0.3)])])
Properties.Material.Add(strMaterialName="Stainless _Steel",
                        listMaterialProperty=[Density([(DENSITY,
                                                        7.75e-09)]),
                                              Elastic([(YOUNGS _MODULUS,
                                                        193000.0),
                                                       (POISSONS _RATIO,
                                                        0.31)])])
Properties.Material.Add(strMaterialName="Titanium _Alloy",
                        listMaterialProperty=[Density([(DENSITY,
                                                        4.62e-09)]),
                                              Elastic([(YOUNGS _MODULUS,
                                                        96000.0),
                                                       (POISSONS _RATIO,
                                                        0.36)])])
Properties.Material.Add(strMaterialName="Aluminum _Alloy",
                        listMaterialProperty=[Density([(DENSITY,
                                                        2.7699999999999997e-09)]),
                                              Elastic([(YOUNGS _MODULUS,
                                                        71000.0),
                                                       (POISSONS _RATIO,
                                                        0.33)])])

Properties.Solid(crlTargets=[Part(3)],
                 strName="Cube _3",
                 iPropertyColor=16131973,
                 crMaterial=Material(1),
                 iCordM=-2,
                 dDynaRemeshVal1=DFLT _DBL,
                 dDynaRemeshVal2=DFLT _DBL,
                 dDispHG=DFLT _DBL,
                 iFLG=-1)
Properties.Solid(crlTargets=[Part(4)],
                 strName="Cube _4",
                 iPropertyId=2,
                 iPropertyColor=10176523,
                 crMaterial=Material(2),
                 iCordM=-2,
                 dDynaRemeshVal1=DFLT _DBL,
                 dDynaRemeshVal2=DFLT _DBL,
                 dDispHG=DFLT _DBL,
                 iFLG=-1)
Properties.Solid(crlTargets=[Part(7)],
                 strName="Cube _7",
                 iPropertyId=3,
                 iPropertyColor=4185823,
                 crMaterial=Material(3),
                 iCordM=-2,
                 dDynaRemeshVal1=DFLT _DBL,
                 dDynaRemeshVal2=DFLT _DBL,
                 dDispHG=DFLT _DBL,
                 iFLG=-1)
Properties.Solid(crlTargets=[Part(8)],
                 strName="Cube _8",
                 iPropertyId=4,
                 iPropertyColor=14470647,
                 crMaterial=Material(4),
                 iCordM=-2,
                 dDynaRemeshVal1=DFLT _DBL,
                 dDynaRemeshVal2=DFLT _DBL,
                 dDispHG=DFLT _DBL,
                 iFLG=-1)

Properties.Shell(crlTargets=[Part(1)],
                 strName="Cube _1",
                 iPropertyId=5,
                 iPropertyColor=6438968,
                 crMatMembrane=Material(5),
                 crMatBend=Material(5),
                 crMatShear=Material(5),
                 dMatOrient1=DFLT _DBL,
                 dThickness=0.001,
                 dBendStiff=DFLT _DBL,
                 dThickRatio=DFLT _DBL,
                 dNSM=DFLT _DBL,
                 dFiberDist1=DFLT _DBL,
                 dFiberDist2=DFLT _DBL,
                 dPlateOff=DFLT _DBL,
                 iItgPts=DFLT _INT)
Properties.Shell(crlTargets=[Part(2)],
                 strName="Cube _2",
                 iPropertyId=6,
                 iPropertyColor=12901905,
                 crMatMembrane=Material(6),
                 crMatBend=Material(6),
                 crMatShear=Material(6),
                 dMatOrient1=DFLT _DBL,
                 dThickness=0.001,
                 dBendStiff=DFLT _DBL,
                 dThickRatio=DFLT _DBL,
                 dNSM=DFLT _DBL,
                 dFiberDist1=DFLT _DBL,
                 dFiberDist2=DFLT _DBL,
                 dPlateOff=DFLT _DBL,
                 iItgPts=DFLT _INT)
Properties.Shell(crlTargets=[Part(5)],
                 strName="Cube _5",
                 iPropertyId=7,
                 iPropertyColor=13102932,
                 crMatMembrane=Material(7),
                 crMatBend=Material(7),
                 crMatShear=Material(7),
                 dMatOrient1=DFLT _DBL,
                 dThickness=0.001,
                 dBendStiff=DFLT _DBL,
                 dThickRatio=DFLT _DBL,
                 dNSM=DFLT _DBL,
                 dFiberDist1=DFLT _DBL,
                 dFiberDist2=DFLT _DBL,
                 dPlateOff=DFLT _DBL,
                 iItgPts=DFLT _INT)
Properties.Shell(crlTargets=[Part(6)],
                 strName="Cube _6",
                 iPropertyId=8,
                 iPropertyColor=652495,
                 crMatMembrane=Material(7),
                 crMatBend=Material(7),
                 crMatShear=Material(7),
                 dMatOrient1=DFLT _DBL,
                 dThickness=0.001,
                 dBendStiff=DFLT _DBL,
                 dThickRatio=DFLT _DBL,
                 dNSM=DFLT _DBL,
                 dFiberDist1=DFLT _DBL,
                 dFiberDist2=DFLT _DBL,
                 dPlateOff=DFLT _DBL,
                 iItgPts=DFLT _INT)

Groups.RightClick.CreateMatGroup()
Groups.RightClick.PropertyGroup()

mat _group = JPT.GetGroupFromSubGroup("Material Group 1")
JPT.Debugger(mat _group)

prop _group = JPT.GetGroupFromSubGroup("Property Group 1")
JPT.Debugger(prop _group)
```
