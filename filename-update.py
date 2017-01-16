import os

root_directory = 'c:/dev/hugosite/content/'

for dir, subdir, files in os.walk(root_directory):
    for filename in files:
        print filename
        year = filename[0:4]
        month = filename[5:7]
        day = filename[8:10]
        datestring = '"' + year + '-' + month + '-' + day +'"' + '\n'
        newname = filename[11:]
        print datestring + ' --  Title:  ' + newname + '   Path:  ' + dir

        f = open(os.path.join(dir,filename),"r")
        contents = f.readlines()
        f.close

	slugname,extension = os.path.splitext(newname)

        contents.insert(2,"date:  " + datestring)
	contents.insert(3,"aliases: " + '["/' +year+'/'+month+'/'+day+"/"+slugname+'/"]' + '\n')

        f = open(os.path.join(dir,newname),"w")
	for line in contents:
		if line.startswith('banner'):
			continue
		if line.startswith('status'):
			continue
		f.write(line)
	f.close()

	os.remove(os.path.join(dir,filename))
