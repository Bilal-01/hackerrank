# Kangroo Jump

def kangrooJump(x1, v1, x2, v2):
    if x1 == x2:
        return "YES"
    if (v1 < v2):
        return "NO"
    if (v1 == 0 or v2 == 0):
        return "NO"

    num = x2 - x1
    den = v1 - v2

    if(v1 == v2):
        return "NO"

    if(num%den == 0):
        return "YES"
    return "NO"

if __name__ == "__main__":
  x1 = 0
  v1 = 2
  x2 = 5
  v2 = 3


  ans = kangrooJump(x1, v1, x2, v2)
  print(ans)