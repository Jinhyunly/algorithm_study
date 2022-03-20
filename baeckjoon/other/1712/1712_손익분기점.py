a,b,c = map(int, input().split())

# 생산되는 대 수가 늘어날 때마다 C와 B의 차이만큼 수입과 비용의 차이가 줄어들게 되고

# 따라서, A/(C-B) 대 생산했을 때 수입과 비용이 같아지기 때문에 +1부터 수입이 많아지게 된다.

if b>=c:
  print(-1)
else:
  print(int(a/(c-b))+1)