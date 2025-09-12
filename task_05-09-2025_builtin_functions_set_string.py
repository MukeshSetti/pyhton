#-------------------------------------String Methods----------------------------------
s = 'Python is a programming language'

print(len(s))          # 32 → length of string
print(s.lower())       # python is a programming language
print(s.upper())       # PYTHON IS A PROGRAMMING LANGUAGE
print(s.capitalize())  # Python is a programming language
print(s.title())       # Python Is A Programming Language

print(s.count('a'))    # 3 → counts occurrences of 'a'
print(s.find('is'))    # 7 → index where 'is' starts
print(s.startswith('Py')) # True
print(s.endswith('age'))  # True
print(s.replace('Python', 'Java')) # Java is a programming language

st = '   Hello '
print(st.strip())   # Hello  → removes both side spaces
print(st.lstrip())  # Hello   → removes left spaces
print(st.rstrip())  #    Hello → removes right spaces

#------------------------------------------set Built-in functions-------------------
a = {1, 2, 3}
b = {3, 4, 5}

print(len(a))        # 3 → number of elements
a.add(6)
print(a)             # {1, 2, 3, 6}

a.remove(2)
print(a)             # {1, 3, 6}
a.discard(10)        # No error if not found

print(a.union(b))        # {1, 3, 4, 5, 6}
print(a.intersection(b)) # {3}
print(a.difference(b))   # {1, 6}
print(a.symmetric_difference(b)) # {1, 4, 5, 6}

print(a.issubset({1,3,6,7}))     # True
print(a.issuperset({1,3}))       # True
print(a.isdisjoint({7,8}))       # True

a.clear()
print(a)   # set() → empty set
