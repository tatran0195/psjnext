# Title:   Analysis.ExportAdx()
# Desc:    Export the ADVENTURECluster solver file in adx format with the existing Job in Assembly Tree. By pointing out the desired ADVC Job in Assembly Tree, exporting could be done multiple times with user's setting
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/analysis/Analysis.ExportAdx
# ---
Geometry.Part.Cube()
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
                 iPropertyColor=16131973,
                 crMaterial=Material(1),
                 iCordM=-2,
                 dDynaRemeshVal1=DFLT_DBL,
                 dDynaRemeshVal2=DFLT_DBL,
                 dDispHG=DFLT_DBL,
                 iFLG=-1)

BoundaryConditions.FixedConstraint(crlTargets=[Face(24)])
BoundaryConditions.Pressure.General(dPressure=1000000.0,
                                    crlTargets=[Face(21,
                                                     23)])

Analysis.ADVC.MakeProcess.Static(strName="ADVC_DEFAULT_PROCESS",
                                 advcStructTimeStep=ADVC_STRUCT_TIME_STEP(dMaxDt=1.0,
                                                                          dMinDt=1e-05),
                                 dStabilizationFactor=DFLT_DBL,
                                 listLoadNode=[],
                                 listLoadCaseNode=[],
                                 listLoadNodeContact=[],
                                 listAdvcRefStressResult=[])

Analysis.ADVC.MakeProcess.Static(strName="ADVC_DEFAULT_PROCESS",
                                 advcStructTimeStep=ADVC_STRUCT_TIME_STEP(dMaxDt=1.0,
                                                                          dMinDt=1e-05),
                                 dStabilizationFactor=DFLT_DBL,
                                 crEdit=ADVCProcessStatic(1),
                                 listLoadNode=[],
                                 listLoadCaseNode=[],
                                 listLoadNodeContact=[],
                                 listAdvcRefStressResult=[])

Analysis.ADVC.MakeProcess.Static(strName="ADVC_DEFAULT_PROCESS",
                                 advcStructTimeStep=ADVC_STRUCT_TIME_STEP(dMaxDt=1.0,
                                                                          dMinDt=1e-05),
                                 dStabilizationFactor=DFLT_DBL,
                                 crEdit=ADVCProcessStatic(1),
                                 listLoadNode=[],
                                 listLoadCaseNode=[],
                                 listLoadNodeContact=[],
                                 listAdvcRefStressResult=[])

Analysis.ADVC.Structure(strPath="D:/Job_1.adx",
                        strName="Job_1",
                        crlProcessSequence=[ADVCProcessStatic(1)],
                        crlTargets=[Part(1)],
                        bAutoAssignDummyProp=True,
                        listLoadNodeContact=[],
                        iNumType=2,
                        iUiPrecision=5)

exported_status = Analysis.ExportAdx(crJob=ADVCJob(1),  # [hl:start]
                                     strPath="D:/Job_2.adx",
                                     iNumType=2,
                                     iUiPrecision=5)  # [hl:end]

JPT.Debugger(exported_status)
