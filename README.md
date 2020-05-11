# Databricks Labs TestDataGenerator
[Release Notes](RELEASE_NOTES.md) |
[Python Wheel](dist/) |
[Developer Docs](python/docs/APIDOCS.md) |
[Examples](examples) |
[Tutorial](tutorial) |
[Contributors](#core-contribution-team)


## Project Description
This Databricks Labs project is a non-supported end-to-end framework for automating the generation of test data 
using the Spark framework. 

It supports:
* Generating test data for all of the 
Spark SQL supported primitive types as a Spark data frame which may be persisted, 
saved to external storage or 
used in other computations
* Limiting numeric values to specific ranges and intervals
* Generation of discrete values - both numeric and text
* Generation of values at random and based on the values of other fields
* Generating multiple values following the same pattern
* Generating arrays of values for ML style feature arrays
* Applying weights to the occurence of values
* Generating values to conform to a schema or independent of an existing schema
* use of SQL expressions in test data generation

 

## Project Support
Please note that all projects in the /databrickslabs github account are provided for your exploration only, and are not formally supported by Databricks with Service Level Agreements (SLAs).  They are provided AS-IS and we do not make any guarantees of any kind.  Please do not submit a support ticket relating to any issues arising from the use of these projects.

Any issues discovered through the use of this project should be filed as GitHub Issues on the Repo.  They will be reviewed as time permits, but there are no formal SLAs for support.

## Compatibility
The code base must be built with Python 3.x. 

For full library compatibility for a specific Databricks Spark release, see the Databricks 
release notes for library compatibility

- https://docs.databricks.com/release-notes/runtime/releases.html

## Building the code

Run  `make clean dist` from the main project directory.

## Running unit tests

If using an evironment with multiple Python versions, make sure to use virtual env or similar to pick up correct python versions.

If necessary, set `PYSPARK_PYTHON` and `PYSPARK_DRIVER_PYTHON` to point to correct versions of Python.

Run  `make install tests` from the main project directory to run the unit tests.

## Using the Project
To use the project, the generated wheel should be installed in your Python notebook as a wheel based library

Once the library has been installed, you can use it to generate a test data frame.

For example

```buildoutcfg
df_spec = (datagen.DataGenerator(sparkSession=spark, name="test_data_set1", rows=cls.row_count,
                                                  partitions=4)
                            .withIdOutput()
                            .withColumn("r", FloatType(), expr="floor(rand() * 350) * (86400 + 3600)",
                                        numColumns=cls.column_count)
                            .withColumn("code1", IntegerType(), min=100, max=200)
                            .withColumn("code2", IntegerType(), min=0, max=10)
                            .withColumn("code3", StringType(), values=['a', 'b', 'c'])
                            .withColumn("code4", StringType(), values=['a', 'b', 'c'], random=True)
                            .withColumn("code5", StringType(), values=['a', 'b', 'c'], random=True, weights=[9, 1, 1])

                            )
                            
df = df_spec.build()
num_rows=df.count()                          
```

## Feedback

Issues with the application?  Found a bug?  Have a great idea for an addition?
Feel free to file an issue.

## Core Contribution team
* Lead Developer, co-designer: Ronan Stokes,RSA, Databricks
* Design: Daniel Tomes, RSA Practice Leader, Databricks