# Title:   Analysis.Nastran.ModalTransientResponse()
# Desc:    Export the input file for Nastran Modal Transient Response Analysis (SOL 112)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/analysis/Analysis.Nastran.ModalTransientResponse
# ---
Geometry.Part.Cube()
Meshing.SolidMeshing(crlParts=[Part(1)], bTet10=True, dGradingFactor=1.05,
     dStretchLimit=0.1, iSpeedVsQual=1, iRegion=1, bSafeMode=False,
     iParallel=12, bInternalMeshOnly=False, iPartColor=65280)

Properties.Material.Add("Structural_Steel", [Density([(DENSITY, 7.85e-09)]),
     Elastic([(YOUNGS_MODULUS, 200000.0), (POISSONS_RATIO, 0.3)])])
Properties.Solid(crMaterial=Material(1), dDynaRemeshVal1=DFLT_DBL,
     dDynaRemeshVal2=DFLT_DBL, dDispHG=DFLT_DBL, crlTargets=[Part(1)], iFLG=-1)

BoundaryConditions.FixedConstraint(crlTargets=[Face(25)])
BoundaryConditions.Pressure.General(dPressure=10.0, dlDirection=[0.0, 0.0, -1.0],
     crlTargets=[Face(26)])

nastran_param = NASTRAN_ANALYSIS(iSolverType=1, iGridFormatType=1, dEpsilon=DFLT_DBL,
     iMaxNumOfIter=DFLT_INT, iMemory=DFLT_INT, iNcpu=1, iSolNo=112,
    nastranOutputRequest=NASTRAN_OUTPUT_REQUEST(iTypeStress=0, iTypeStrain=0),
    nastranNonlinear=NASTRAN_NONLINEAR(bUseEPSW=True))
Analysis.Nastran.ModalTransientResponse(nastranAnalysis= nastran_param,strPath="D:/Job_1.bdf")  # [hl]
