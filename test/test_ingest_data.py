import unittest

from ingest_data import ingest_data


class TestIngestData(unittest.TestCase):
    def test_file_invalid(self):
        # assertRaises(Error esperado, función a testear, argumentos)
        self.assertRaises(
            FileNotFoundError, ingest_data, "test/samples/non_existent_file.csv"
        )

    def test_single_data_file(self):
        x = ingest_data("test/samples/single-data-file.csv")
        # assertEqual(Valor actual , valor esperado)
        self.assertEqual(len(x), 1)

    def test_header_file(self):
        x = ingest_data("test/samples/header-file.csv")
        # assertEqual(Valor actual , valor esperado)
        self.assertEqual(len(x), 0)

    def test_not_supported_file(self):
        # assertRaises(Error esperado, función a testear, argumentos)
        self.assertRaises(UnicodeDecodeError, ingest_data, "test/samples/data.xlsx")

    def test_different_header_file(self):
        # assertRaises(Error esperado, función a testear, argumentos)
        self.assertRaises(
            KeyError, ingest_data, "test/samples/different-header-file.csv"
        )
