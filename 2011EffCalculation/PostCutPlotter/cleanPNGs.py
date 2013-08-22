#!/usr/bin/python

from os.path import isfile
from os import listdir, makedirs
from sys import exit
from tempfile import mkdtemp  # Secure methods of generating random directories
from shutil import move

php = """<?php 
if ($handle = opendir('.')) {
    /* This is the correct way to loop over the directory. */
    while (false !== ($file = readdir($handle))) {
        $ext = end(explode('.', $file));
        if($ext == "jpg" || $ext == "png") {
            echo "$file";
            echo "<img src=\\"$file\\" alt=\\"Image\\" />";
        }
    }
    closedir($handle);
}
?>
"""

histotypes = [
                "Z0MassFine",  # Putting this first is a nasty, brutish hack to avoid Z0Mass matching Z0MassFine
                "Z0Mass",
                "Z0Rapidity",
                "Z0pt",
                "e0pt",
                "e1pt",
                "e0eta",
                "e1eta",
                "e0phi",
                "e1phi",
                "phistar",
                "pileup"
             ]

# Make a list of all the png files
pngs = [f for f in listdir('.') if (isfile(f) and f.endswith('.png'))]
if not pngs:
    exit("No PNGs, so exiting.")

# Make the directories 
tmpdir = mkdtemp(suffix="", prefix="plots_", dir='.')
print "Making directory to store the plots: ",tmpdir

if tmpdir:
    for h in histotypes:
        makedirs(tmpdir + '/' + h)
        # Write an index page so we can look at the folders easily in a web
        # browser
        f = open(tmpdir + '/' + h + '/index.php', "w")
        f.write(php)
        f.close()

# Move PNGs into sub directories
for png in pngs:
    for h in histotypes:
        if h in png:
            move(png, tmpdir + '/' + h + '/' + png)
            break
