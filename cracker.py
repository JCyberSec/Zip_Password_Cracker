import zipfile

zipfilename = 'zipNameHere.zip' # Change this to link to zip required to crack
dictionary = 'dictFileHere.txt' # Change this to file with passwords in to use

password = None
password1 = 1
zip_file = zipfile.ZipFile(zipfilename)
with open(dictionary, 'r') as f:
        for line in f.readlines():
                password = line.strip('\n')
                print password
                if password1 == 1:
                        try:
                                zip_file.extractall(pwd=password)
                                password1 = 'Password found: %s' % password
                        except:
                                pass
                else:
                        print "PASSWORD = " + password1
                        break
print "PASSWORD = " + password1

