"""
Relocates the files for a given version of Isotope from vendor/isotope
into a Django app for use with Django staticfiles.
"""
import subprocess
import sys

DEFAULT_VERSION = "1.5.18"


def cp(src):
    cmd = [
        "cp -R vendor/isotope/%s isotope/static/isotope/" % src,
    ]
    subprocess.call(cmd, shell=True)


def main():
    args = {
        "version": DEFAULT_VERSION if len(sys.argv) is 1 else sys.argv[1],
    }
    subprocess.call(["mkdir -p ./isotope/static/isotope"], shell=True)
    subprocess.call(
            ["cd vendor/isotope && git checkout v%(version)s" %args],
            shell=True)
    cp("/jquery.isotope*.js")

    with open("./VERSION", "w") as f:
        f.write(args["version"])


if __name__ == "__main__":
    main()
