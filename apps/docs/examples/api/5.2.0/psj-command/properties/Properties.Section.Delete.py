# Title:   Properties.Section.Delete()
# Desc:    Delete the create property sections in 1D properties section library
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/properties/Properties.Section.Delete
# ---
Properties.Section.AddGeneral(strName="abc", 
                              iSecGenType=2, 
                              dDsecGensizeT1=0.02)

creating_status = Properties.Section.Delete(crlSections=[SectionGeneral(1)])  # [hl]

JPT.Debugger(creating_status)
