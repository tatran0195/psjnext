---
title: "Groups.RightClick.PropertyGroup()"
description: "Create a group of properties to the Group tree in the Group Window"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Groups > RightClick > PropertyGroup"
---

## Description

Create a group of properties to the Group tree in the Group Window.

## Syntax

```psj
Groups.RightClick.PropertyGroup(...)
```

## Inputs

This function does not require any input values.

## Return Code

A _List of Cursor_ specifying all the created groups.

## Sample Code

```psj {46}
Geometry.Part.Cube()

Meshing.SolidMeshing(crlParts=[Part(1)], 
                     bTet10=True, 
                     dGradingFactor=1.05, 
                     dStretchLimit=0.1,
                     iSpeedVsQual=1, 
                     iRegion=1, 
                     bSafeMode=False, 
                     iParallel=8, 
                     bInternalMeshOnly=False, 
                     iPartColor=65280)

Properties.Material.Add("Structural _Steel", 
                        [Density([(DENSITY, 
                                   7.849999999999999e-09)]),
                         Elastic([(YOUNGS _MODULUS, 
                                   200000.0), 
                                  (POISSONS _RATIO, 
                                   0.3)])])

Properties.Solid(strName="Solid Property 1", 
                 crMaterial=Material(1), 
                 iCordM=-2, 
                 dDynaRemeshVal1=DFLT _DBL, 
                 dDynaRemeshVal2=DFLT _DBL, 
                 dDispHG=DFLT _DBL,
                 crlTargets=[Part(1)], 
                 iFLG=-1)

Properties.Shell(strName="Shell Property 1", 
                 crMatMembrane=Material(1), 
                 crMatBend=Material(1), 
                 crMatShear=Material(1), 
                 dMatOrient1=DFLT _DBL,  
                 dThickness=0.001, 
                 dBendStiff=DFLT _DBL, 
                 dThickRatio=DFLT _DBL, 
                 dNSM=DFLT _DBL,
                 dFiberDist1=DFLT _DBL, 
                 dFiberDist2=DFLT _DBL, 
                 dPlateOff=DFLT _DBL, 
                 iItgPts=DFLT _INT, 
                 crlTargets=[Face(21)])

created _groups = Groups.RightClick.PropertyGroup()

JPT.Debugger(created _groups)
```
