import unittest
from parameterized import parameterized
from find_substrings import is_matching_concat_string_pair


class FindSubstringsTest(unittest.TestCase):

  @parameterized.expand([
    (
        'simple strings', ['Hello', 'World', 'GoodbyeHello'], 'GoodbyeHello',
        True),
    ('simple strings', ['A', 'B', 'C', 'A'], 'AD', False),
    ('simple strings', ['B', 'C', 'A', 'D'], 'DB', True),
    ('simple strings', ['A', 'A', 'C', 'AA'], 'AAC', True)
  ])
  def test_find_concatenation_simple(self, name, strings,
      desired_concatenated_string,
      expected_found):
    actual_found = is_matching_concat_string_pair(strings,
                                                  desired_concatenated_string)
    message = 'For input values: {0}, desired_concatenated_string = \'{1}\', expected value = {2}, and actual value = {3}'.format(
        strings, desired_concatenated_string, expected_found, actual_found)
    self.assertEqual(expected_found, actual_found, message)

  @parameterized.expand([
    ('ordered list', ['A', 'B', 'E', 'F'], 'BF', True),
    ('ordered list', ['P', 'Q', 'U', 'V'], 'QU', True),
    ('ordered list', ['H', 'M', 'O', 'P'], 'NP', False),
    ('ordered list', ['A', 'D', 'L', 'H'], 'DFH', False)
  ])
  def test_find_concatenation_ordered(self, name, strings,
      desired_concatenated_string,
      expected_found):
    actual_found = is_matching_concat_string_pair(strings,
                                                  desired_concatenated_string)
    message = 'For input values: {0}, desired_concatenated_string = \'{1}\', expected value = {2}, and actual value = {3}'.format(
        strings, desired_concatenated_string, expected_found, actual_found)
    self.assertEqual(expected_found, actual_found, message)

  @parameterized.expand([
    ('unordered list', ['A', 'F', 'B', 'E'], 'BF', True),
    ('unordered list', ['Q', 'P', 'V', 'U'], 'QU', True),
    ('unordered list', ['P', 'M', 'O', 'H'], 'NP', False),
    ('unordered list', ['H', 'L', 'D', 'A'], 'DFH', False)
  ])
  def test_find_concatenation_unordered(self, name, strings,
      desired_concatenated_string,
      expected_found):
    actual_found = is_matching_concat_string_pair(strings,
                                                  desired_concatenated_string)
    message = 'For input values: {0}, desired_concatenated_string = \'{1}\', expected value = {2}, and actual value = {3}'.format(
        strings, desired_concatenated_string, expected_found, actual_found)
    self.assertEqual(expected_found, actual_found, message)

  @parameterized.expand([
    ('list with duplicates', ['A', 'A', 'B', 'F'], 'AF', True),
    ('list with duplicates', ['P', 'Q', 'P', 'V'], 'QO', False),
    ('list with duplicates', ['H', 'R', 'O', 'P', 'R'], 'RP', True),
    ('list with duplicates', ['A', 'L', 'L', 'H'], 'LLH', False)
  ])
  def test_find_concatenation_duplicates(self, name, strings,
      desired_concatenated_string,
      expected_found):
    actual_found = is_matching_concat_string_pair(strings,
                                                  desired_concatenated_string)
    message = 'For input values: {0}, desired_concatenated_string = \'{1}\', expected value = {2}, and actual value = {3}'.format(
        strings, desired_concatenated_string, expected_found, actual_found)
    self.assertEqual(expected_found, actual_found, message)

  @parameterized.expand([
    ('list with empty string', ['A', '', 'B', 'F'], 'F', True),
    ('list with empty string', ['P', 'Q', '', 'V'], 'QO', False)
  ])
  def test_find_concatenation_edgecase(self, name, strings,
      desired_concatenated_string,
      expected_found):
    actual_found = is_matching_concat_string_pair(strings,
                                                  desired_concatenated_string)
    message = 'For input values: {0}, desired_concatenated_string = \'{1}\', expected value = {2}, and actual value = {3}'.format(
        strings, desired_concatenated_string, expected_found, actual_found)
    self.assertEqual(expected_found, actual_found, message)

  @parameterized.expand([
    ('list with large number of strings',
     ['FQI', 'ZSR', 'YRU', 'SJZ', 'NOY', 'NCE', 'CEJ', 'GFN', 'ILC', 'DLX',
      'BMS', 'YZS', 'CCG', 'LMJ', 'KNZ', 'LPL', 'OIB', 'ASS', 'CKT', 'VQY',
      'FJC', 'VRZ', 'WGY', 'BRY', 'UVE', 'KTR', 'GRL', 'PZC', 'WIE', 'CDM',
      'AHT', 'NXQ', 'YSS', 'SRL', 'WVR', 'BDB', 'HOK', 'EHY', 'JBO', 'UCW',
      'QKU', 'CQD', 'OGQ', 'BTH', 'CJI', 'JQX', 'XWX', 'MCB', 'NWP', 'CZI'],
     'CJIVRZ', True),
    ('list with large number of strings',
     ['9DP', 'MVQ', 'A9T', 'CRZ', 'CI8', 'QT1', 'D0F', 'SSX', 'PRK', 'LKH',
      'YCW', 'VNU', 'D6F', 'JMX', 'ACT', '15E', '4QQ', 'QK3', 'R6E', '1A7',
      '46X', 'M1M', 'KNJ', 'R3B', 'WAS', 'AN9', '2QN', '7M7', 'GMU', '5R8',
      'FKG', 'KAG', 'XZR', '9BN', 'KMS', '1ZB', 'WXC', 'KH1', 'SIV', 'RLT',
      'SDX', 'LGW', 'DU5', 'LDT', 'GQ7', 'JMM', 'CZN', 'GCU', 'HYT', '0UF',
      'Q48', 'XDG', 'WOI', 'USX', 'VOU', '08W', 'QGJ', 'NDS', '67U', '9YU',
      '1KO', 'Z58', 'JYM', 'JWX', 'A45', 'OV4', '8VG', 'UHV', '1AX', 'WBQ',
      'GAV', 'QS0', 'Z99', 'MM7', 'J4T', 'XZK', 'NHR', '8K1', 'W8O', 'YC0',
      'V57', 'NT7', 'ZMI', 'UKV', '485', 'P18', 'HVM', 'PSG', 'EE0', 'M1U',
      'TFR', 'XQN', 'ZL6', 'T19', 'KDM', 'YBU', 'YC7', 'G0L', 'FYD', 'U1T'],
     'LGW1DP', False)
  ])
  def test_find_concatenation_large_input_sequence(self, name, strings,
      desired_concatenated_string,
      expected_found):
    actual_found = is_matching_concat_string_pair(strings,
                                                  desired_concatenated_string)
    message = 'For input values: {0}, desired_concatenated_string = \'{1}\', expected value = {2}, and actual value = {3}'.format(
        strings, desired_concatenated_string, expected_found, actual_found)
    self.assertEqual(expected_found, actual_found, message)
