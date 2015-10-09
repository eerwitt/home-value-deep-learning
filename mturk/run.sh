#!/bin/bash
# Load a set of hits based on a tsv generated using `build_mt_tsv.py`.
JAVA_HOME=/usr ./aws-mturk-clt-1.3.1/bin/loadHITs.sh \
  -input ./input/images_with_ids.tsv \
  -question ./conf/category.question \
  -properties ./conf/category.properties \
  -sandbox
