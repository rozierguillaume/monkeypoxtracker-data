#!/bin/bash

# source: https://stackoverflow.com/questions/11929766/how-to-delete-all-git-commits-except-the-last-five/11931881

b="$(git branch --no-color | cut -c3-)" 
h="$(git rev-parse $b)" 
echo "Current branch: $b $h" 
c="$(git rev-parse $b~15)" 
echo "Recreating $b branch with initial commit $c ..." 
git checkout --orphan new-start $c 
git commit -C $c 
git rebase --onto new-start $c $b 
git branch -d new-start 
git gc
