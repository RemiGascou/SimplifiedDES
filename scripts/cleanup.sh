#!/bin/bash

#basedir="~/Documents/git_projects/SimplifiedDES/"
basedir="/media/administrateur/C29EAD659EAD5329/Documents/git_projects/SimplifiedDES/"
cd $basedir
cd lib
for dir in $(find "$basedir" -mindepth 1 -type d); do
		if [[ $dir == *"__pycache__" ]]; then
			echo "Removing" $dir
			rm -rf $dir
		fi
done
for fpyc in $(find "$basedir" -mindepth 1 -type f); do
		if [[ $fpyc == *".pyc" ]]; then
			echo "Removing" $fpyc
			rm $fpyc
		fi
done
