students = {
  'Theodore': 19,
  'Roxanne': 22,
  'Mathew': 21,
  'Betty': 20
}
def test(d):
      return max(d, key = d.get), min(d, key = d.get)
print(test(students))