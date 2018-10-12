def reconstruct_trip(tickets):
  # pass 
  my_dict = {}
  my_route = ['']* (len(tickets) - 1)
  for ticket in tickets:
    my_dict[ticket[0]] = ticket[1]
    if ticket[0] is None:
      my_route[0] = ticket[1]
  for i in range(1, len(my_route)):
    if my_route[i - 1] in my_dict:
      my_route[i] = my_dict[my_route[i - 1]]
    else:
      return []
  return my_route

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  pass
