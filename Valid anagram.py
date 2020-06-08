
class Solution:

  def isAnagram(self, s, t):
    if len(s) != len(t):
      return False
    table = [0] * 26
    start = ord('a')
    for sc, tc in zip(s, t):
      table[ord(sc) - start] += 1
      table[ord(tc) - start] -= 1
    for v in table:
      if v != 0:
        return False
    return True

  def isAnagram0(self, s, t):
    if len(s) != len(t):
      return False
    hash_map = {}
    for sc, tc in zip(s, t):
      hash_map[sc] = hash_map.get(sc, 0) + 1
      hash_map[tc] = hash_map.get(tc, 0) - 1
    for v in hash_map.values():
      if v != 0:
        return False
    return True
