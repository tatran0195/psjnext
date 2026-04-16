# Title:   Analysis.TSSolver.NormalModes()
# Desc:    Export the Input Deck for TechnoStar Normal Modes analysis (SOL 103)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/analysis/Analysis.TSSolver.NormalModes
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

input_param = NASTRAN_ANALYSIS(iSolverType=3, 
                               iGridFormatType=1, 
                               dEpsilon=DFLT_DBL,
                               iMaxNumOfIter=DFLT_INT, 
                               iMemory=1024, 
                               iSolNo=103,
                               nastranEigen=NASTRAN_EIGEN(dStartFreq=0.0, 
                                                          dEndFreq=100.0, 
                                                          iNoOfModes=3),
                               nastranEigen126=NASTRAN_EIGEN126(dMLDSStartFreq=0.0, 
                                                                dMLDSEndFreq=100.0, 
                                                                iMLDSNoOfModes=3),
                               nastranOutputRequest=NASTRAN_OUTPUT_REQUEST(iTypeStress=0, 
                                                                           iTypeStrain=0),
                               nastranSettings=NASTRAN_SETTINGS(iMLDS=2), 
                               nastranNonlinear=NASTRAN_NONLINEAR(bUseEPSW=True))

export_status = Analysis.TSSolver.NormalModes(nastranAnalysis = input_param,   # [hl]
                                              strPath = re.sub(re.escape("\\"), "/", environ["Temp"]) + \  # [hl]
                                                        "/TechnoStar/Test.bdf")  # [hl]

JPT.Debugger(export_status)
