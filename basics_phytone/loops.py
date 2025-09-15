# For Loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
# Looping Through a String
for x in "banana":
  print(x)
# The break Statement
fruits = ["apple", "ananas", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print("b:" + x)
# The continue Statement
fruits = ["apple", "ananas", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print("c:" + x)
# The range() Function
for x in range(6):
  print("d:" + str(x))
#Using the start parameter:
for x in range(2, 6):
  print("dp:" + str(x))
#Using the step parameter:
for x in range(2, 30, 3): # will print numbers from 2 to 30, with a step of 3
  print("dps:" + str(x))
# The else Statement
for x in range(6):
  print("e:" + str(x))
else:
  print("Finally finished!")
# Nested Loops
adj = ["red", "big", "tasty"]
for x in adj:
  for y in fruits:
    print(x, y)
# The pass Statement
for x in [0, 1, 2]:
  pass  # Do nothing, placeholder for future code
print("f:pass statement executed")
# while Loop
i = 1
while i < 6:
  print("g:" + str(i))
  i += 1
# The break Statement
i = 1
while i < 6:
  print("h:" + str(i))
  if i == 3:
    break
  i += 1
# The continue Statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print("j:" + str(i))
# The else Statement
i = 1
while i < 6:
  print("k:" + str(i))
  i += 1
else:
  print("Finally finished!")