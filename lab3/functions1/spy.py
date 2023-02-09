def findCombination(nums: list):
  res = ""
  for i in nums:
    if i == 0 or i == 7:
      res+=str(i)

  if res.find("007") == -1:
      return False
  else:
      return True

l = [1, 0, 0, 7]
print(findCombination(l))