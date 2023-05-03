import os
import pikepdf
import logging
import coloredlogs

#CHANGE PASSWORD HERE
pdf_password = "0"

#Logs to scriptName.log
scriptName = os.path.basename(__file__)
logging.basicConfig(level = logging.DEBUG,
                    filename = scriptName + ".log",
                    filemode = "a",
                    encoding = 'utf-8',
                    format = '[%(asctime)s] [%(levelname)s] %(message)s')

#Logs into console
mylogs = logging.getLogger(__name__)
stream = logging.StreamHandler()
mylogs.addHandler(stream)
coloredlogs.install(level=logging.DEBUG, 
                    logger=mylogs,
                    fmt='[%(asctime)s] [%(levelname)s] %(message)s')

# rootdir = os.getcwd()
# nb = 0
# for subdir, dirs, files in os.walk(rootdir):
#     for file in files:
#         filepath = subdir + os.sep + file
#         if filepath.endswith(".pdf"):
#             nb += 1
#             mylogs.info(str(nb) + ") File processing : " + file + " (" + filepath +")")
            #Check if th PDF is password locked
pass_start = "81887"
years = ["98", "97", "96", "95", "94", "93", "92"]
for year in years:
    for month in range(1, 12):
        if len(str(month)) == 1:
            month = "0" + str(month)
        else:
            month = str(month)
        for date in range(1, 31):
            if len(str(date)) == 1:
                date = "0" + str(date)
            else:
                date = str(date)
            pdf_password = pass_start + date + month + year
            file = "8716053960030112022.pdf"
            try:
                pdf = pikepdf.open(file)
                mylogs.info(file + " isn't lock with a password")
            except pikepdf._qpdf.PasswordError:
                #If locked, try to unlock with password line 7
                try:
                    pdf = pikepdf.open(file, password=pdf_password, allow_overwriting_input=True)
                    print(f"Password : {pdf_password}")
                    pdf.save(file)
                    mylogs.info ("Successfully remove password on " + file)
                    break
                except pikepdf._qpdf.PasswordError:
                    # pass
                    mylogs.error (f"Bad password {pdf_password} for " + file)
                except: #default
                    mylogs.error ("Failed to remove password on " + file)
os.system("pause")