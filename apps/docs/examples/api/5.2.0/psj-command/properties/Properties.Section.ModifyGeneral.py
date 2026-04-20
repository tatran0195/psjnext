# Title:   Properties.Section.ModifyGeneral()
# Desc:    Modify the existing general section for 1D Property.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/properties/Properties.Section.ModifyGeneral
# ---
Properties.Section.AddGeneral(  strName="t1", 
                                iSecGenType=2, 
                                dDsecGensizeT1=0.001, 
                                iDirType=1)
Properties.Section.ModifyGeneral(strName="t1",   # [hl:start]
                                crSection=SectionGeneral(1), 
                                iGeneralType=2, 
                                dT1=0.001, 
                                iDirType=3)  # [hl:end]
