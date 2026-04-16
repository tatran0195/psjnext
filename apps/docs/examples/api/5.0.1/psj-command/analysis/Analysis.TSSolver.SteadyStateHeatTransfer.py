# Title:   Analysis.TSSolver.SteadyStateHeatTransfer()
# Desc:    Export the Input Deck for TechnoStar Steady State Heat Transfer analysis (SOL 153)
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/analysis/Analysis.TSSolver.SteadyStateHeatTransfer
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

BoundaryConditions.BoundaryTemperature.Constant(dFTemp=373.15, 
                                                crlTargets=[Face(24)])
BoundaryConditions.HeatFlux.SurfaceFlux(strName="SurfaceHeatFlux1", 
                                        dFflux=150000.0,
                                        iDistributionMethod=1, 
                                        crTable=None, 
                                        crlTargets=[Face(23)])

input_param = NASTRAN_ANALYSIS(iSolverType=3, 
                               iGridFormatType=1, 
                               bUseCASI=True, 
                               dEpsilon=1e-13,
                               iMaxNumOfIter=500, 
                               iMemory=1024, 
                               iSolNo=153,
                               nastranOutputRequest=NASTRAN_OUTPUT_REQUEST(iTypeThermal=1, 
                                                                           iTypeFlux=6))

export_status = Analysis.TSSolver.SteadyStateHeatTransfer(nastranAnalysis = input_param,   # [hl]
                                                          strPath = re.sub(re.escape("\\"), "/", environ["Temp"]) + \  # [hl]
                                                                    "/TechnoStar/Test.bdf")  # [hl]

JPT.Debugger(export_status)
