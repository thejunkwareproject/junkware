#!/bin/bash

#    USAGE :
#
#    chmod +x run_tests.sh
#    ./run_tests.sh          # run all tests
#    ./run_tests.sh xxx.py   # run a single test
#

test_dir=`pwd`/tests
testfile=$1

run_all () {
    echo >&2 "$@"
    for entry in "$test_dir"/*
    do
        if [ -f "$entry" ];  
        then
            file="${entry##*/}"
            if [[ "$file" == test_* ]] && [[ "$file" != *pyc ]] && [[ "$file" == *py ]]
            then
                # echo $file
                nosetests --rednose --force-color ${entry}
            fi
        fi
    done
    exit 1
}

run_one () {
    

    # test extension 
    if test ${testfile##*.} != "py"; then die "Invalid file extension. File should be *.py"; fi

    # launch script
    nosetests --rednose --force-color $test_dir/${testfile##*/}
}

die () {
    echo >&2 "$@"
    exit 1
}

[ "$#" -eq 1 ] || run_all
run_one