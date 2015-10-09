# MTurk Version of Categorization

At first, I tried using MTurk to do the Categorization of images based on their style. This ended up costing too much money and time (> $300 and unknown time).

MTurk creates hits based on a TSV file which is generated using `build_mt_tsv.py` which stopped being maintained.

The IDs would be read from this file and include a URL which are then put into the `./conf/category.question`.
