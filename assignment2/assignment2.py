# Refactor code
# -------------
# Not timed (good to get it back within 24 hours)
#
# An intern has provided the code below to update the version number
# within two different files.
# The intern has left and you need to review and improve the code before
# submitting to source control.
#
# Please do not be constrained by the existing code (i.e. you don't have
# to keep the same function names, structure)
# Aim for production quality 'best-practice/clean' code
#
# Original Requirements
# ---------------------
# A script in a build process needs to update the build version number in 2
# locations.
# - The version number will be in an environment variable "BuildNum"
# - The files to be modified will be under "$SourcePath/develop/global/src"
# directory
# - The "SConstruct" file has a line "point=123," (where 123
# (just an example) should be updated with the value of "BuildNum"
# Environment variable)
# - The "VERSION"file has a line "ADLMSDK_VERSION_POINT= 123" (where 123
# (just an example) should be updated with the value of "BuildNum"
# Environment variable)

import os
import re


# SCONSTRUCT file interesting lines
# config.version = Version(
# major=15,
# minor=0,
# point=6,
# patch=0
#)
def updateSconstruct():
    # Update the build number in the SConstruct file
    os.chmod(os.path.join(os.environ["SourcePath"],"develop","global","src","SConstruct"), 0o0755)
    fin = open(os.path.join(os.environ["SourcePath"],"develop","global","src","SConstruct"), 'r')
    fout = open(os.path.join(os.environ["SourcePath"],"develop","global","src","SConstruct1"), 'w')
    for line in fin:
        line=re.sub("point\=[\d]+","point="+os.environ["BuildNum"],line)
        fout.write(line)
    fin.close()
    fout.close()
    os.remove(os.path.join(os.environ["SourcePath"],"develop","global","src","SConstruct"))
    os.rename(os.path.join(os.environ["SourcePath"],"develop","global","src","SConstruct1"),
        os.path.join(os.environ["SourcePath"],"develop","global","src","SConstruct"))

# VERSION file interesting line
# ADLMSDK_VERSION_POINT=6
def updateVersion():
    # Update the build number in the VERSION file

    os.chmod(os.path.join(os.environ["SourcePath"],"develop","global","src","VERSION"), 0o0755)
    fin = open(os.path.join(os.environ["SourcePath"],"develop","global","src","VERSION"), 'r')
    fout = open(os.path.join(os.environ["SourcePath"],"develop","global","src","VERSION1"), 'w')
    for line in fin:
        line=re.sub("ADLMSDK_VERSION_POINT=[\d]+","ADLMSDK_VERSION_POINT="+os.environ["BuildNum"],line)
    fout.write(line)
    fin.close()
    fout.close()
    os.remove(os.path.join(os.environ["SourcePath"],"develop","global","src","VERSION"))
    os.rename(os.path.join(os.environ["SourcePath"],"develop","global","src","VERSION1"),
    os.path.join(os.environ["SourcePath"],"develop","global","src","VERSION"))


def updateBuildNumber(path, pattern, buildNum):
    # Update the build number in the file at `path` with `buildNum` located at the line matching `pattern`

    tmp_path = path + ".tmp"
    reg = re.compile(pattern + "[\\d]+")

    os.chmod(path, 0o0755)
    fin = open(path, 'r')
    fout = open(tmp_path, 'w')
    for line in fin:
        line = reg.sub(pattern + str(buildNum), line)
        fout.write(line)
    fin.close()
    fout.close()
    os.remove(path)
    os.rename(tmp_path, path)


def main():
    buildNumber = os.environ["BuildNum"]
    srcPath = os.path.join(os.environ["SourcePath"], "develop", "global", "src")

    # updateSconstruct()
    sconstructPath = os.path.join(srcPath, "SConstruct")
    sconstructPattern = "point\=[\d]+"
    updateBuildNumber(sconstructPath, sconstructPattern, buildNumber)

    # updateVersion()
    versionPath = os.path.join(srcPath, "VERSION")
    versionPattern = "ADLMSDK_VERSION_POINT=[\d]+"
    updateBuildNumber(versionPath, versionPattern, buildNumber)


if __name__ == "__main__":
    main()
