######################################################################
mdlint-compat 0.1.0
Phil Yeeles <phil@yeel.es>
Last updated: 2024-02-27
License: CC0
######################################################################

import fileinput,subprocess,os,re,sys,pip

# Install pymarkdownlnt if not already available
try:
    __import__("pymarkdown.api")
except ImportError:
    pip.main(['install','pymarkdownlnt'])

ns=0
doc=""
f=sys.argv[1]
snippets=[]
skip=False
snip=""

for line in fileinput.input(f):
    if skip:
        snip+=line
        if re.search(r'^<!--\s*markdownlint-enable',line):
            snippets.append(snip)
            snip=""
            skip=False
    else:
        if re.search(r'^<!--\s*markdownlint-disable',line):
            skip=True
            snip+=line
            line="@@@@LINTIGNORE_"+str(ns)+"@@@@\n"
            ns+=1
        doc+=line

tmpfile=f+".linttmp.md"
tmp=open(tmpfile,"a")
tmp.write(doc)
tmp.close()

subprocess.run(["pymarkdownlnt","fix",tmpfile])

outdoc=""

for line in fileinput.input(tmpfile):
    if re.search(r'^@@@@LINTIGNORE_\d+@@@@$',line):
        line=snippets[int(re.sub(r'^@@@@LINTIGNORE_(\d+)@@@@$',r'\1',line))]
    outdoc+=line


outfile=f+".fixed.md"
out=open(outfile,"a")
out.write(outdoc)
out.close()

os.remove(tmpfile)
