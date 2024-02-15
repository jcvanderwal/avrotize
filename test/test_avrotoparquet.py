import os
import sys
from os import path, getcwd

current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))
sys.path.append(project_root)

import unittest
from unittest.mock import patch
from avrotize.avrotoparquet import convert_avro_to_parquet

class TestAvroToParquet(unittest.TestCase):
    def test_convert_address_avsc_to_kusto(self):
        cwd = os.getcwd()        
        avro_path = os.path.join(cwd, "test", "avsc", "address.avsc")
        parquet_path = os.path.join(cwd, "test", "tmp", "address.parquet")
        dir = os.path.dirname(parquet_path)
        if not os.path.exists(dir):
            os.makedirs(dir)
        
        convert_avro_to_parquet(avro_path, None, parquet_path, False)           

    def test_convert_telemetry_avsc_to_kusto(self):
        cwd = os.getcwd()        
        avro_path = os.path.join(cwd, "test", "avsc", "telemetry.avsc")
        parquet_path = os.path.join(cwd, "test", "tmp", "telemetry.parquet")
        dir = os.path.dirname(parquet_path)
        if not os.path.exists(dir):
            os.makedirs(dir)
        
        convert_avro_to_parquet(avro_path, None, parquet_path, True)
