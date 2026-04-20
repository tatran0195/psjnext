# Title:   Analysis.Nastran.DirectFrequencyResponse()
# Desc:    Export the input file for Nastran Direct Frequency Response Analysis (SOL 108)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/analysis/Analysis.Nastran.DirectFrequencyResponse
# ---
Geometry.Part.Cube(iPartColor=6409934)
Meshing.AdjustCircleVertex(crlParts=[Part(1)], bInModeSurfaceMesh=True)
Meshing.SetMeshAttribute(
    crlParts=[Part(1)], 
    surfaceMesh=SURFACE_MESH(
        dGeomAngle=0.7853981634, 
        iPerformanceMode=1, 
        dAutoMergeTinyFacesAngle=0.5235987756, 
        bGeomApprox=True))
Meshing.SurfaceMeshing(
    crlParts=[Part(1)], 
    surfaceMesh=SURFACE_MESH(
        dGeomAngle=0.7853981634, 
        iPerformanceMode=1, 
        dAutoMergeTinyFacesAngle=0.5235987756, 
        bGeomApprox=True), 
    iThreadNum=16)
Properties.Material.Add(
        strMaterialName="Structural_Steel", 
        dictMaterialProperty={
            'Density': {'density': {'DENSITY': [7850.000000000001]}}, 
            'Elastic': {'elastic': {'YOUNGS_MODULUS': [200000000000.0], 
            'POISSONS_RATIO': [0.3]}}, 
            'Expansion': {'expansion': {'ALPHA': [1.2e-05]}}, 
            'Conductivity': {'conductivity': {'CONDUCTIVITY': [59.0]}}, 
            'SpecificHeat': {'specificHeat': {'SPECIFIC_HEAT': [461.0]}}}, 
        iMaterialID=5, 
        iMaterialColor=10264731)
BoundaryConditions.FixedConstraint(strName="Constraint_1", crlTargets=[Node(491, 489, 490, 492)])
BoundaryConditions.Force.General(
    strName="Force_1", 
    forceLBC=FORCE_LBC(vecForce=[DFLT_DBL, DFLT_DBL, 55.555556]), 
    crlTargets=[Node(495)])
BoundaryConditions.Force.General(
    strName="Force_2", 
    forceLBC=FORCE_LBC(vecForce=[DFLT_DBL, DFLT_DBL, 88.555556]), 
    crlTargets=[Node(494)])
MeshEdit.CreateNode.Offset(vecOffset=[0.0, 0.0, -0.001], crlNodes=[Node(491)])
Connections.SpringsDampers.Spring.OneToOne.sameDoFs(
    iMethod=17, 
    strName="Spring_1", 
    crlMasterTargets=[Node(491)], 
    crlSlaveTargets=[Node(515)], 
    iSpringType=2, d
    Tolerance=DFLT_DBL, 
    posTStiffness=[1000000, 1.7976931e+308, 1.7976931e+308], 
    posRStiffness=[1.7976931e+308, 1.7976931e+308, 1.7976931e+308])
Connections.MassElements(
    strName="Mass_1", 
    crlTargets=[Node(513)], 
    dMass=36779.0, 
    iDof=6, 
    bDesigner=False, 
    dInertia0=DFLT_DBL, 
    dInertia1=DFLT_DBL, 
    dInertia2=DFLT_DBL, 
    dInertia3=DFLT_DBL, 
    dInertia4=DFLT_DBL, 
    dInertia5=DFLT_DBL)
BoundaryConditions.FieldData(
    strName="FieldData1", 
    iType=4, 
    ilSheet=[10, 2, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0])
Properties.Shell(
    crlTargets=[Part(1)], 
    strName="ShellProperty_1", 
    iPropertyColor=16131973, 
    crMatMembrane=Material(5), 
    crMatBend=Material(5), 
    crMatShear=Material(5), 
    dThickness=0.0003)
ret = Analysis.Nastran.DirectFrequencyResponse(  # [hl:start]
    strName="SOL108", 
    strDescription="SOL108", 
    nastranAnalysis=NASTRAN_ANALYSIS(
        iSolverType=1, 
        iGridFormatType=1, 
        bDeleteFloatingNodes=True, 
        bContinuanceMarker=True, 
        dEpsilon=DFLT_DBL, 
        iMaxNumOfIter=DFLT_INT, 
        iMemory=2, 
        iNcpu=1, 
        iSolNo=108, 
        nastranFrequency=NASTRAN_FREQUENCY(iTableId=1), 
        nastranOutputRequest=NASTRAN_OUTPUT_REQUEST(
            iValueSdisplacement=DFLT_INT, 
            iValueAcceleration=DFLT_INT, 
            iValueVelocity=DFLT_INT, 
            iTypeDisplacement=9, 
            iTypeStress=9, 
            iTypeStrain=0), 
        nastranCaseControl=NASTRAN_CASE_CONTROL(
            strTitle="NAS_SUPPORT_CARD_FOR_SOL108"), 
        nastranSettings=NASTRAN_SETTINGS(
            iAUTOSPC=1, 
            strGRDPNT="0", 
            strK6ROT="1.000000", 
            iBAILOUT=-1, 
            iMEFFMASS=1, 
            dCUTOFF_VALUE=5.5), 
        nastranSubcase=[NASTRAN_SUBCASE(
            iId=1, 
            strTitle="Subcase1", 
            iSubcaseIdForDload=DFLT_INT, 
            iSubcaseIdForSpc=DFLT_INT)]), 
    bDummyPropAutoAssign=True, 
    iDummyPropMaterialID=5, 
    strPath="C:/temp/SOL108.bdf", 
    bOutputXYPlots=True, 
    iOutputDOFType=4, 
    iXYPlotDisplacementType=264, 
    iXYPlotVelocityType=264, 
    iXYPlotAccelerationType=264, 
    strYTitle="ACCE PSD", 
    bOutputGeomIDofDummyProp=True)  # [hl:end]
print(ret)
