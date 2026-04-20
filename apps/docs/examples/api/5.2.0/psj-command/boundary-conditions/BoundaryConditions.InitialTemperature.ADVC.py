# Title:   BoundaryConditions.InitialTemperature.ADVC()
# Desc:    Read the temperature result output from format of Adventure Cluster solver and defines it as the initial temperature
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/boundary-conditions/BoundaryConditions.InitialTemperature.ADVC
# ---
import os

temp_folder = os.environ["Temp"] + "/TechnoStar"

if os.path.isdir(temp_folder):
    pass
else:
    os.mkdir(temp_folder)

Geometry.Part.Cube(iPartColor=6473570)
BoundaryConditions.BoundaryTemperature.Constant(dFTemp=293.15, 
                                                crlTargets=[Part(1)])
Properties.Material.Add("Structural_Steel", 
                        [Density([(DENSITY, 
                                   7.85e-09)]), 
                        Elastic([(YOUNGS_MODULUS, 
                                  200000.0), 
                                 (POISSONS_RATIO, 
                                  0.3)])])
Properties.Shell(crlTargets=[Part(1)], 
                 strName="Shell Property 1", 
                 iPropertyColor=16131973, 
                 crMatMembrane=Material(1), 
                 crMatBend=Material(1), 
                 crMatShear=Material(1), 
                 dMatOrient1=DFLT_DBL, 
                 dThickness=0.001, 
                 dBendStiff=DFLT_DBL, 
                 dThickRatio=DFLT_DBL, 
                 dNSM=DFLT_DBL, 
                 dFiberDist1=DFLT_DBL, 
                 dFiberDist2=DFLT_DBL, 
                 dPlateOff=DFLT_DBL, 
                 iItgPts=DFLT_INT)
Analysis.ADVC.MakeProcess.SteadyState(strName="ADVC_DEFAULT_PROCESS", 
                                      advcHeatTimeStep=ADVC_HEAT_TIME_STEP(dMaxdt=1.0, 
                                                                           dMindt=1e-05))
Analysis.ADVC.MakeProcess.SteadyState(strName="ADVC_DEFAULT_PROCESS", 
                                      advcHeatTimeStep=ADVC_HEAT_TIME_STEP(dMaxdt=1.0, 
                                                                           dMindt=1e-05), 
                                      crEdit=ADVCProcessSSH(1), 
                                      listLoadNode=[ADVC_LOAD_NODE(cr=LbcTempBoundary(1))])
Analysis.ADVC.MakeProcess.SteadyState(strName="ADVC_DEFAULT_PROCESS", 
                                      advcHeatTimeStep=ADVC_HEAT_TIME_STEP(dMaxdt=1.0, 
                                                                           dMindt=1e-05), 
                                      crEdit=ADVCProcessSSH(1))
Analysis.ADVC.HeatTransfer(strPath=temp_folder + "/test.adx", 
                           strName="Job_1", 
                           crlProcessSequence=[ADVCProcessSSH(1)], 
                           crlTargets=[Part(1)], 
                           bAutoAssignDummyProp=True, 
                           crDummyPropMaterial=Material(1), 
                           listLoadNodeContact=[], 
                           iUiPrecision=6, 
                           bExportGeometryID=True)

JPT.Exec('New Document()')

Geometry.Part.Cube()

created_bcs = BoundaryConditions.InitialTemperature.ADVC(  # [hl:start]
    strName="InitialTemperature_1",
    iLocalTemperatureUnit=1, 
    strFilePathName = temp_folder \
                      + "/test.adx", 
    crlTargets=[Part(1)])  # [hl:end]

JPT.Debugger(created_bcs)
