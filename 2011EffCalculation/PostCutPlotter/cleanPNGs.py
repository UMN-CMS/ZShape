#!/usr/bin/python

from os.path import isfile
from os import listdir, makedirs
from sys import exit
from tempfile import mkdtemp  # Secure methods of generating random directories
from shutil import move

php = """<?php 
// Code from:                                                                                     
// http://stackoverflow.com/questions/5471392/display-images-from-a-folder-in-a-specific-order/5471427#5471427

// Find all files in that folder                                                                  
$files = glob('*');

// Do a natural case insensitive sort, usually 1.jpg and 10.jpg would come next                   
// to each other with a regular sort                                                              
natcasesort($files);

// Opening HTML
echo "<html>\\n";
echo "  <head>\\n";
echo "    <meta http-equiv=\\"cache-control\\" content=\\"max-age=0\\" />\\n";
echo "    <meta http-equiv=\\"cache-control\\" content=\\"no-cache\\" />\\n";
echo "    <meta http-equiv=\\"expires\\" content=\\"0\\" />\\n";
echo "    <meta http-equiv=\\"expires\\" content=\\"Tue, 01 Jan 1980 1:00:00 GMT\\" />\\n";
echo "    <meta http-equiv=\\"pragma\\" content=\\"no-cache\\" />\\n";
echo "    <meta name=\\"robots\\" content=\\"noindex\\">\\n <!-- Prevent indexing -->\\n";
echo "    <meta http-equiv=\\"Content-Type\\" content=\\"text/html; charset=utf-8\\" />\\n";
echo "  </head>\\n";
echo "  <body>\\n";
echo "    <div class=\\"content\\">\\n";

// Display images 
foreach($files as $file) {
        $ext = end(explode('.', $file));
        if($ext == "jpg" || $ext == "png") {
            echo "      <hr><br>\\n";
            echo "      <h1>$file</h1><br>\\n";
            echo "      <img src=\\"$file\\" alt=\\"Image\\" /><br>\\n";
        }
}

// Final line and closing HTML
echo "      <hr>\\n";
echo "    </div>\\n";
echo "  </body>\\n";
echo "</html>\\n";
?>"""

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
