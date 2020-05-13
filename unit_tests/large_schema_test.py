from pyspark.sql.types import StructType, StructField, IntegerType, StringType, FloatType, TimestampType, DecimalType
from pyspark.sql.types import BooleanType, DateType
import databrickslabs_testdatagenerator as datagen
from pyspark.sql import SparkSession
import unittest


schema = StructType([
StructField("PK1",StringType(),True),
StructField("XYYZ_IDS",StringType(),True),
StructField("R_ID",IntegerType(),True),
StructField("CL_ID",StringType(),True),
StructField("INGEST_DATE",TimestampType(),True),
StructField("CMPY_ID",DecimalType(38,0),True),
StructField("TXN_ID",DecimalType(38,0),True),
StructField("SEQUENCE_NUMBER",DecimalType(38,0),True),
StructField("DETAIL_ORDER",DecimalType(38,0),True),
StructField("TX_T_ID",DecimalType(38,0),True),
StructField("TXN_DATE",TimestampType(),True),
StructField("AN_ID",DecimalType(38,0),True),
StructField("ANC_ID",DecimalType(38,0),True),
StructField("ANV_ID",DecimalType(38,0),True),
StructField("ANE_ID",DecimalType(38,0),True),
StructField("AND_ID",DecimalType(38,0),True),
StructField("APM_ID",DecimalType(38,0),True),
StructField("ACL_ID",DecimalType(38,0),True),
StructField("MEMO_TEXT",StringType(),True),
StructField("ITEM_ID",DecimalType(38,0),True),
StructField("ITEM2_ID",DecimalType(38,0),True),
StructField("V1_BASE",DecimalType(38,9),True),
StructField("V1_YTD_AMT",DecimalType(38,9),True),
StructField("V1_YTD_HOURS",DecimalType(38,0),True),
StructField("ISTT",DecimalType(38,9),True),
StructField("XXX_AMT",StringType(),True),
StructField("XXX_BASE",StringType(),True),
StructField("XXX_ISTT",StringType(),True),
StructField("HOURS",DecimalType(38,0),True),
StructField("STATE",DecimalType(38,0),True),
StructField("LSTATE",DecimalType(38,0),True),
StructField("XXX_JURISDICTION_ID",DecimalType(38,0),True),
StructField("XXY_JURISDICTION_ID",DecimalType(38,0),True),
StructField("AS_OF_DATE",TimestampType(),True),
StructField("IS_PAYOUT",StringType(),True),
StructField("IS_PYRL_LIABILITY",StringType(),True),
StructField("IS_PYRL_SUMMARY",StringType(),True),
StructField("PYRL_LIABILITY_DATE",TimestampType(),True),
StructField("PYRL_LIAB_BEGIN_DATE",TimestampType(),True),
StructField("QTY",DecimalType(38,9),True),
StructField("RATE",DecimalType(38,9),True),
StructField("AMOUNT",DecimalType(38,9),True),
StructField("SPERCENT",DecimalType(38,9),True),
StructField("DOC_XREF",StringType(),True),
StructField("IS_A",StringType(),True),
StructField("IS_S",StringType(),True),
StructField("IS_CP",StringType(),True),
StructField("IS_VP",StringType(),True),
StructField("IS_B",StringType(),True),
StructField("IS_EX",StringType(),True),
StructField("IS_I",StringType(),True),
StructField("IS_CL",StringType(),True),
StructField("IS_DPD",StringType(),True),
StructField("IS_DPD2",StringType(),True),
StructField("DPD_ID",DecimalType(38,0),True),
StructField("IS_NP",StringType(),True),
StructField("TAXABLE_TYPE",DecimalType(38,0),True),
StructField("IS_ARP",StringType(),True),
StructField("IS_APP",StringType(),True),
StructField("BALANCE1",DecimalType(38,9),True),
StructField("BALANCE2",DecimalType(38,9),True),
StructField("IS_FLAG1",StringType(),True),
StructField("IS_FLAG2",StringType(),True),
StructField("STATEMENT_ID",DecimalType(38,0),True),
StructField("INVOICE_ID",DecimalType(38,0),True),
StructField("STATEMENT_DATE",TimestampType(),True),
StructField("INVOICE_DATE",TimestampType(),True),
StructField("DUE_DATE",TimestampType(),True),
StructField("EXAMPLE1_ID",DecimalType(38,0),True),
StructField("EXAMPLE2_ID",DecimalType(38,0),True),
StructField("IS_FLAG3",StringType(),True),
StructField("ANOTHER_ID",DecimalType(38,0),True),
StructField("MARKUP",DecimalType(38,9),True),
StructField("S_DATE",TimestampType(),True),
StructField("SD_TYPE",DecimalType(38,0),True),
StructField("SOURCE_TXN_ID",DecimalType(38,0),True),
StructField("SOURCE_TXN_SEQUENCE",DecimalType(38,0),True),
StructField("PAID_DATE",TimestampType(),True),
StructField("OFX_TXN_ID",DecimalType(38,0),True),
StructField("OFX_MATCH_FLAG",DecimalType(38,0),True),
StructField("OLB_MATCH_MODE",DecimalType(38,0),True),
StructField("OLB_MATCH_AMOUNT",DecimalType(38,9),True),
StructField("OLB_RULE_ID",DecimalType(38,0),True),
StructField("ETMMODE",DecimalType(38,0),True),
StructField("DDA_ID",DecimalType(38,0),True),
StructField("DDL_STATUS",DecimalType(38,0),True),
StructField("ICFS",DecimalType(38,0),True),
StructField("CREATE_DATE",TimestampType(),True),
StructField("CREATE_USER_ID",DecimalType(38,0),True),
StructField("LAST_MODIFY_DATE",TimestampType(),True),
StructField("LAST_MODIFY_USER_ID",DecimalType(38,0),True),
StructField("EDIT_SEQUENCE",DecimalType(38,0),True),
StructField("ADDED_AUDIT_ID",DecimalType(38,0),True),
StructField("AUDIT_ID",DecimalType(38,0),True),
StructField("AUDIT_FLAG",StringType(),True),
StructField("EXCEPTION_FLAG",StringType(),True),
StructField("IS_PENALTY",StringType(),True),
StructField("IS_INTEREST",StringType(),True),
StructField("NET_AMOUNT",DecimalType(38,9),True),
StructField("TAX_AMOUNT",DecimalType(38,9),True),
StructField("TAX_CODE_ID",DecimalType(38,0),True),
StructField("TAX_RATE_ID",DecimalType(38,0),True),
StructField("CURRENCY_TYPE",DecimalType(38,0),True),
StructField("EXCHANGE_RATE",DecimalType(38,9),True),
StructField("HOME_AMOUNT",DecimalType(38,9),True),
StructField("HOME_OPEN_BALANCE",DecimalType(38,9),True),
StructField("IS_FOREX_GAIN_LOSS",StringType(),True),
StructField("SPECIAL_TAX_TYPE",DecimalType(38,0),True),
StructField("SPECIAL_TAX_OPEN_BALANCE",DecimalType(38,9),True),
StructField("TAX_OVERRIDE_DELTA_AMOUNT",DecimalType(38,9),True),
StructField("INCLUSIVE_AMOUNT",DecimalType(38,9),True),
StructField("CUSTOM_ACCOUNT_TAX_AMT",DecimalType(38,9),True),
StructField("J_CODE_ID",DecimalType(38,0),True),
StructField("DISCOUNT_ID",DecimalType(38,0),True),
StructField("DISCOUNT_AMOUNT",DecimalType(38,9),True),
StructField("TXN_DISCOUNT_AMOUNT",DecimalType(38,9),True),
StructField("SUBTOTAL_AMOUNT",DecimalType(38,9),True),
StructField("LINE_DETAIL_TYPE",DecimalType(38,0),True),
StructField("W_RATE_ID",DecimalType(38,0),True),
StructField("R_QUANTITY",DecimalType(38,9),True),
StructField("R_AMOUNT",DecimalType(38,9),True),
StructField("SRC_QTY_USED",DecimalType(38,9),True),
StructField("SRC_AMT_USED",DecimalType(38,9),True),
StructField("LM_CLOSED",StringType(),True),
StructField("CUSTOM_FIELD_VALUES",StringType(),True),
StructField("PROGRESS_TRACKING_TYPE",DecimalType(38,0),True),
StructField("ITEM_RATE_TYPE",DecimalType(38,0),True),
StructField("CUSTOM_FIELD_VALS",StringType(),True),
StructField("REGION_C_CODE",StringType(),True),
StructField("LAST_MODIFIED_UTC",TimestampType(),True),
StructField("date",DateType(),True),
StructField("yearMonth",StringType(),True),
StructField("isDeleted",BooleanType(),True)
])


print("schema", schema)

spark = SparkSession.builder \
    .master("local[4]") \
    .appName("spark unit tests") \
    .config("spark.sql.warehouse.dir", "/tmp/spark-warehouse") \
    .getOrCreate()

# Test manipulation and generation of test data for a large schema
class TestLargeSchemaOperation(unittest.TestCase):
    testDataSpec = None
    dfTestData = None
    row_count = 100000

    def setUp(self):
        print("setting up")

    @classmethod
    def setUpClass(cls):
        cls.testDataSpec = (datagen.DataGenerator(sparkSession=spark, name="test_data_set1", rows=cls.row_count,
                                                  partitions=4)
                            .withSchema(schema)
                            .withIdOutput()
                            )

        print("Test generation plan")
        print("=============================")
        cls.testDataSpec.explain()

        print("=============================")
        print("")
        cls.dfTestData = cls.testDataSpec.build().cache()

    def test_simple_data(self):
        self.dfTestData.limit(30).show()

    def test_generated_data_count(self):
        count = self.dfTestData.count()
        self.assertEqual(count, self.row_count)

    def test_distinct_count(self):
        distinct_count = self.dfTestData.select('id').distinct().count()
        self.assertEqual(distinct_count, self.row_count)

    def test_script_table(self):
        tableScript=self.testDataSpec.scriptTable("testTable")
        print("tableScript", tableScript)

    def test_large_clone(self):
        sale_values = ['RETAIL', 'ONLINE', 'WHOLESALE', 'RETURN']
        sale_weights = [1, 5, 5, 1]

        ds = (self.testDataSpec.clone().setRowCount(1000)
              .withColumnSpecs(patterns=".*_ID", match_types=StringType(), format="%010d", min=1, max=123, step=1)
              .withColumnSpecs(patterns=".*_IDS", match_types=StringType(), format="%010d", min=1, max=100, step=1)
              .withColumnSpec("R_ID", min=1, max=100, step=1)
              .withColumnSpec("XYYZ_IDS", min=1, max=123, step=1,
                              format="%05d")  # .withColumnSpec("nstr4", percent_nulls=10.0, min=1, max=9, step=2,  format="%04d")
              # example of IS_SALE
              .withColumnSpec("IS_S", values=sale_values, weights=sale_weights, random=True)
              # .withColumnSpec("nstr4", percent_nulls=10.0, min=1, max=9, step=2,  format="%04d")

              )

        ds.compute_build_plan()
        ds.explain()
        df = ds.build()
        df.show()










# run the tests
# if __name__ == '__main__':
#  print("Trying to run tests")
#  unittest.main(argv=['first-arg-is-ignored'],verbosity=2,exit=False)

# def runTests(suites):
#    suite = unittest.TestSuite()
#    result = unittest.TestResult()
#    for testSuite in suites:
#        suite.addTest(unittest.makeSuite(testSuite))
#    runner = unittest.TextTestRunner()
#    print(runner.run(suite))


# runTests([TestBasicOperation])
