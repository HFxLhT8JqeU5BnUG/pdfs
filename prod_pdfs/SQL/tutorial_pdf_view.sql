create or replace view test_schema.tutorial_pdf_view AS 
select int_col::text, varchar_col, timestamp_col::text, float_col::text
from example_table;