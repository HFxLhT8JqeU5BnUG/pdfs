# PDF Generator Walkthrough

This is a guide on how to get values from a database and generate a filled out PDF form for each row.

First, make sure you have a .env file with the template directory, PDF output directory, and database authentication. It should follow the format of the .env.example file.

Next, get your PDF form template and put it in the template directory. You'll need to know the form fields that you're trying to fill out. If you don't, you can uncomment the following line from pdf.PDF: ```print(self.reader.get_form_text_fields())```

Next, write a view for the database, execute it, and place it in the SQL directory. Not absolutely necessary, but highly recommended.

Next, go to configs and write your mapping and naming configs. If you're aliasing rows from the database, then you don't need a mapping. That's the recommended approach. Otherwise, you can map {"PDF_form_field" : "column_name"} for as many columns as you want to pass to the PDF form.

Naming is pretty much essential. The "static_name" key will be the first part of every output file name. The "dynamic_name_key" will append the value at that column to the file name for each row of data passed. If you don't do this, all the files will have the same name, and so everything will be overwritten by the last PDF generated. Note: Don't be dumb. These are file names. No spaces, periods, other BS. I'm not building safeguards here, so you're on your own if you break the file names.

Now you're ready to write the class that will generate the PDFs. Put it in this directory. Inherit from PdfSuperClass from prod_pdfs. The initialize() function must be overwritten. You must assign the "table" and "template" attributes here. Table can be a table, but should be the name of your view. And while we're here talking about the database stuff- schema is also optional, will default to public/no schema.

If you chose a mapping and/or naming config, assign them in the initialize function with table and template. 

If you're not applying a mapping, the data will be passed as it is gathered from the database (after transformations, if applicable). Extra columns don't break the program, but will be disregarded when PDFs are generated.

After you've set the attributes, make sure that initialize() returns True.

Optionally, you can override the transform() function. This will perform any kind of Python transformations you'd like to the rows from the database BEFORE applying the mapping. What this means:

The database interface returns a list of dictionaries from the table/view you select. Each dictionary is a column_name : value mapping. The transform() function can be used to apply conditional logic, regex, etc. on this data. After the transform() call, the data will be mapped according to the mapping (if applicable) and then sent to the PDF form.

Finally, import the new PDF form class to prod_pdfs.central. Place it in the pdf_dict under the name you would like to use when calling it as a CLI arg.

To build the image (from the pdfs directory):

```sudo docker build -t pdfs .```

## NOTE

I'm putting this before the instructions on how to run the container. Please, for the love of god, follow a standardized naming convention and use the import structure demonstrated in the tutorial. Please document your SQL stuff. 

### Runtime Docker flags:

```-v ./OUTPUT_DIR:/app/OUTPUT_DIR```

This will mount OUTPUT_DIR to the OUTPUT_DIR specified in the .env file. This is where PDFs generated will be stored.

```--network host```

This allows you to access the host network. REQUIRED if accessing a localhost database.


### Runtime container flags:

```-m <pdf_module_to_run>```

This is how you specify which PDF class to call. It calls it according to the dictionary key in prod_pdfs.pdf_dict.

```-t <test_name>```

For internal use. Used to run tests specified in the test directory.


### Example usage:

Let's say you have a locally hosted postgres database, with the table and view specified the sibling SQL directory, you built the image with the name "pdfs", and you want to run the tutorial PDF class and send the output to ~/pdfs/OUTPUT_DIR.

```sudo docker run -v ./OUTPUT_DIR:/app/OUTPUT_DIR --network host pdfs -m tutorial```


