import unittest
import usaddress
import csv

def readAddresses(filename):
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        return [row[0] for row in reader]

def writeAddresses(filename, data):
    with open(filename, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        for item in data:
            writer.writerow([item[0]])

class TestLedcoreUnit(unittest.TestCase):

    def test_lecore_addresses_with_unit(self):
        addrs = readAddresses('measure_performance/test_data/ledcor_unit_test.csv')
        parsed = [(addr,usaddress.parse(addr)) for addr in addrs]

        result = filter(lambda item: not any(c[1] == 'OccupancyIdentifier' for c in item[1]), parsed)

        writeAddresses('measure_performance/test_data/non_match.csv', result)

        tagged = [(addr,usaddress.tag(addr)) for addr in addrs]

        assert len(result) is 0
