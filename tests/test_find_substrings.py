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
