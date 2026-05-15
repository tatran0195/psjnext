---
title: "JPT.RunSunShine()"
description: "Run SunShine to solve an analysis problem"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Run SunShine to solve an analysis problem.

## Syntax

```psj
JPT.RunSunShine(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### InputFile

- Specify the path of solver input file will be solved.

<!-- @since:5.1.0 @optional -->
### OutputFolder

- Specify the path of folder to store the result files.
- The default value is "" (the folder where the input file is located).

<!-- @since:5.1.0 @optional -->
### Memory

- Specify the size of memory in GB to be used in execution.
- The default value is 2.0 (GB).

<!-- @since:5.1.0 @optional -->
### Threads

- Specify the number of threads to be used in execution.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### KeepTemp

- Specify whether to keep the temporary files after termination of execution.
- The default value is False.

<!-- @since:5.1.0 @optional -->
### WriteDatabase

- Specify whether to keep the temporary files after termination of execution.
- The default value is False.

<!-- @since:5.1.0 @optional -->
### ShowProgress

- Specify whether to keep the temporary files after termination of execution.
- The default value is False.

## Return Code

- Boolean specifying whether the process is executed successfully or not:
  - True: The process is executed successfully.
  - False: Cannot execute the function.

## Sample Code

```psj {63-69}
# Prepare model
Geometry.Part.Cube(dlLength=[0.01, 0.01, 0.1], iPartColor=7463537)
Meshing.SetMeshAttribute(crlParts=[Part(1)], 
                        surfaceMesh=SURFACE _MESH(dMaxElemSize=0.4, 
                          dGeomAngle=0.7853981634, 
                          iPerformanceMode=1, 
                          dAutoMergeTinyFacesAngle=0.5235987756, 
                          bGeomApprox=True, 
                          iNextEntityOffsetId=0))
Meshing.SurfaceMeshing(crlParts=[Part(1)], 
                      surfaceMesh=SURFACE _MESH(dMaxElemSize=0.4, 
                        dGeomAngle=0.7853981634, 
                        iPerformanceMode=1, 
                        dAutoMergeTinyFacesAngle=0.5235987756, 
                        bGeomApprox=True, 
                        iNextEntityOffsetId=0), 
                      iThreadNum=16)
Meshing.SolidMeshing(crlParts=[Part(1)], 
                    dGradingFactor=1.05, 
                    dStretchLimit=0.1, 
                    iSpeedVsQual=1, 
                    iRegion=1, 
                    bSafeMode=False, 
                    iParallel=16, 
                    bInternalMeshOnly=False, 
                    iPartColor=65280)
BoundaryConditions.FixedConstraint(strName="Constraint _1", crlTargets=[Face(25)])
BoundaryConditions.Force.General(strName="Force _1", 
                                forceLBC=FORCE _LBC(vecForce=[DFLT _DBL, DFLT _DBL, 100.0]), 
                                  crlTargets=[Face(26)])
Properties.Material.Add(strMaterialName="Structural _Steel",
                       dictMaterialProperty={
                        'Density': {'density': {'DENSITY': [7850.000000000001]}}, 
                        'Elastic': {'elastic': {'YOUNGS _MODULUS': [200000000000.0], 
                        'POISSONS _RATIO': [0.3]}}, 
                        'Expansion': {'expansion': {'ALPHA': [1.2e-05]}}, 
                        'Conductivity': {'conductivity': {'CONDUCTIVITY': [59.0]}}, 
                        'SpecificHeat': {'specificHeat': {'SPECIFIC _HEAT': [461.0]}}}, 
                      iMaterialID=5, 
                      iMaterialColor=10264731)
Properties.Solid(crlTargets=[Part(1)], 
                strName="SolidProperty _1",
                iPropertyColor=959547, 
                crMaterial=Material(5), 
                iCordM=-2, 
                dDynaRemeshVal1=DFLT _DBL, 
                dDynaRemeshVal2=DFLT _DBL, 
                dDispHG=DFLT _DBL, 
                iFLG=-1)
Analysis.TSSS.LinearStatic(
                          nastranAnalysis=NASTRAN _ANALYSIS(
                            iSolverType=6, 
                            iGridFormatType=1, 
                            dEpsilon=DFLT _DBL, 
                            iMaxNumOfIter=DFLT _INT, 
                            iNumberOfThreads=1, 
                            iMemory=2, 
                            iNcpu=DFLT _INT, 
                            iSolNo=101, 
                            nastranOutputRequest=NASTRAN _OUTPUT _REQUEST(iTypeStrain=0)), 
                          strPath="C:/temp/SOL _101.bdf")
# Run SunShine to solve the problem
progress = JPT.RunSunShine(r"C:\\temp\\SOL _101.bdf",
                          "",
                          2,
                          1,
                          False,
                          True,
                          False)
if progress == True:
  print("SunShine succeeded, can start a new document and import the result...")
else:
  print("SunShine failed")
```
