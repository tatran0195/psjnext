# Title:   Analysis.TSSolver.ExportDynamisBdf()
# Desc:    Export the TechnoStar Dynamis solver file in bdf format
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/analysis/Analysis.TSSolver.ExportDynamisBdf
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

dynamic_param = NASTRAN_ANALYSIS(iSolverType=3, 
                                 iGridFormatType=1, 
                                 dEpsilon=DFLT_DBL,
                                 iMaxNumOfIter=DFLT_INT, 
                                 iMemory=DFLT_INT, iNcpu=1, 
                                 iSolNo=101,
                                 nastranOutputRequest=NASTRAN_OUTPUT_REQUEST(iValueBcresults=DFLT_INT,
                                                                             iValueBgresults=DFLT_INT, 
                                                                             iTypeStrain=0),
                                 nastranNonlinear=NASTRAN_NONLINEAR(iKMETHOD=3, 
                                                                    iMAXITER=1, 
                                                                    bUseEPSW=True))

Analysis.TSSolver.Job(nastranAnalysis = dynamic_param)

export_status = Analysis.TSSolver.ExportDynamisBdf(strPath = re.sub(re.escape("\\"), "/", environ["Temp"]) + \  # [hl]
                                                             "/TechnoStar/Test.bdf",   # [hl]
                                                   crJob = DynamisJob(1))  # [hl]

JPT.Debugger(export_status)
