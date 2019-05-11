
def find_substrings_equal_concatenation(string_list, desired_concatenated_string):
  #
  # IMPORTANT:
  # 1. Write your solution in this function
  # 2. Do not make changes to the function signature
  # 3. Use the 'run' command in the IDE, to run the main method. You can also invoke the main method from the terminal.
  # 4. Use the 'run-tests' command in the IDE, to run unit tests.
  return None


def main():
  strings = ['Hello','World','Goodbye']
  desired_concatenated_string = 'GoodbyeHello'
  was_found = find_substrings_equal_concatenation(strings, desired_concatenated_string)
  message = 'Given a list of strings {0}, the function checking whether the list contains a concatenated string \'{1}\' returned value: {2}\n'.format(
      strings, desired_concatenated_string, was_found)
  print(message)


if __name__ == '__main__':
  main()
