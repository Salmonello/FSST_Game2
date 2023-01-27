ba = "hallo***********************************************************"
print(len(ba))
baum = ba +  ('*' * (64  - len(ba)))

print(len(baum), baum)