# Title:   Home.ImportResults.WAON()
# Desc:    Import WAON result file to the Jupiter Database.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post-home/Home.ImportResults.WAON
# ---
#Please set path to your sample WAON file.
filepath="C:/Temp/"
bem_file = filepath + "BEM.bdf"
fpm_file = filepath + "FPM.bdf"
result = base_FILEPATH + "result/"
Home.ImportResults.WAON(bem_file,   # [hl:start]
                        fpm_file, 
                        result, 
                        bReadLoadAndConstraint=True, 
                        bReadConnection=True, 
                        bCreateResultsAtMidNode=True)  # [hl:end]
