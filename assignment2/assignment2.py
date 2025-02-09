import os
import re


def updateBuildNumber(path, pattern, buildNum):
    # Update the build number in the file at `path` with `buildNum` located at the line matching `pattern`

    tmp_path = path + ".tmp"
    reg = re.compile(pattern + "[\\d]+")

    os.chmod(path, 0o0755)

    with open(path, 'r') as fin:
        with open(tmp_path, 'w') as fout:
            for line in fin:
                line = reg.sub(pattern + str(buildNum), line)
                fout.write(line)

    os.remove(path)
    os.rename(tmp_path, path)


def main():
    buildNumber = os.environ["BuildNum"]
    srcPath = os.path.join(os.environ["SourcePath"], "develop", "global", "src")

    # updateSconstruct()
    sconstructPath = os.path.join(srcPath, "SConstruct")
    sconstructPattern = "point="
    updateBuildNumber(sconstructPath, sconstructPattern, buildNumber)

    # updateVersion()
    versionPath = os.path.join(srcPath, "VERSION")
    versionPattern = "ADLMSDK_VERSION_POINT="
    updateBuildNumber(versionPath, versionPattern, buildNumber)


if __name__ == "__main__":
    main()
