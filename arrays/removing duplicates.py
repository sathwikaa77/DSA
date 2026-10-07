def remove_duplicates(arr):
  write = 1
  for read in range(1, len(arr)):
      if arr[read] != arr[read - 1]:
          arr[write] = arr[read]
          write += 1
  return write
numbers = [1, 1, 2, 2, 2, 3, 4, 4, 5 ]
new_length = remove_duplicates(numbers)
print(numbers[ :new_length])
