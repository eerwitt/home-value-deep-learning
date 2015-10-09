# Categorization WebApp

Used to create a training set by categorizing images from Zillow as exterior, interior or a few other choices.

This is a fairly typical Django webapp and it only has one URL:

  http://localhost:8000/cat.html

It will continually show any uncategorized images ~50 at a time. Makes it easy to categorize ~4 images every second.

## Setup

```
pip install -r requirements.txt
python manage.py migrate
```

Once things are setup, open a shell and create some images.

```
python manage.py shell_plus

[0]: Image.objects.create(
  zillow_id="13373_rid",
  url="http://photos2.zillowstatic.com/p_h/IS5ylthesicqd80000000000.jpg")
```

## Finalize Training

After going over all the uncategorized images, we need to output a TSV which can be used in training.

`python manage.py generate_training_file ./output.tsv`

This will create a file named `"output.csv"` which will include all the Zillow IDs, URLs and categories of images which were categorized using this tool.
