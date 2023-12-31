tutorial_mapping = {
    "Given Name Text Box" : "varchar_col",
    "House nr Text Box" : "int_col",
    "Address 2 Text Box" : "timestamp_col",
    "Postcode Text Box" : "float_col",
    "row_num" : "row_num"
}


tutorial_naming = {
    "static_name" : "tutorial",
    "dynamic_name_key" : "row_num"
}


# Note: I'm creating row_num in the transform() call,
# so I need to make sure that the mapping pulls it
# through the write() function after transformation