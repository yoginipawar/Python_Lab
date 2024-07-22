#Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen

def read_file_line_by_line(filename):
  """
  Reads the content of a text file line by line and displays it.

  Args:
      filename: The name of the text file to read.
  """
  try:
    # Open the file in read mode with a context manager
    with open(filename, 'r') as file:
      # Read each line and print it
      for line in file:
        print(line, end='')
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")

# Example usage
read_file_line_by_line("ABC.txt")

#output

Atoms of radioactive elements can split. According to Albert Einstein, mass and energy are interchangeable under certain circumstances. When atoms split, the process is called nuclear fission. In this case, a small amount of mass is converted into energy. Thus the energy released cannot do much damage. However, several subatomic particles called neutrons are also emitted during this process. Each neutron will hit a radioactive element releasing more neutrons in the process. This causes a chain reaction and creates a large amount of energy. This energy is converted into heat which expands uncontrollably causing an explosion. Hence, atoms do not literally explode. They generate energy that can cause explosions.
