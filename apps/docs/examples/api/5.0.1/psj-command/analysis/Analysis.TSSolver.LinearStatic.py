# Title:   Analysis.TSSolver.LinearStatic()
# Desc:    Export the Input Deck for TechnoStar solver Linear Static analysis (SOL 101)
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/analysis/Analysis.TSSolver.LinearStatic
# ---
from os import environ
import re

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

input_param = NASTRAN_ANALYSIS(iSolverType=3, 
                               iGridFormatType=1, 
                               bUseCASI=True, 
                               dEpsilon=DFLT_DBL,
                               iMaxNumOfIter=DFLT_INT, 
                               iMemory=1024, 
                               iSolNo=101,
                               nastranFreqTimestep=NASTRAN_FREQ_TIMESTEP(iDampingType=2, 
                                                                         iModalDampingTableId=0),
                               nastranOutputRequest=NASTRAN_OUTPUT_REQUEST(iTypeStrain=0),
                               nastranNonlinear=NASTRAN_NONLINEAR(iKMETHOD=3, 
                                                                  iMAXITER=DFLT_INT, 
                                                                  bUseEPSW=True, 
                                                                  dEPSU=DFLT_DBL,
                                                                  dEPSP=DFLT_DBL))

export_status = Analysis.TSSolver.LinearStatic(nastranAnalysis = input_param,   # [hl]
                                               strPath = re.sub(re.escape("\\"), "/", environ["Temp"]) + \  # [hl]
                                                         "/TechnoStar/Test.bdf")  # [hl]

JPT.Debugger(export_status)
