[![Python application](https://github.com/HFxLhT8JqeU5BnUG/pdfs/actions/workflows/python-app.yml/badge.svg)](https://github.com/HFxLhT8JqeU5BnUG/pdfs/actions/workflows/python-app.yml)

# PDFS

This is a project to get data from a database and dump it into a fillable PDF from a template. Look at ./prod_pdfs/pdf_generators/tutorial.md and tutorial.py to learn how to generate your own PDFs.

## Build

Don't forget to create a .env file. Follow the format from ./.env.example.

From ~/pdfs:

```sudo docker build -t pdfs .```

To take ownership of output directory after running container (if running container as sudo):

```sudo chown -R $USER ~/pdfs/OUTPUT_DIR```