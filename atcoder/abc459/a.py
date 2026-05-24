helloworld = "HelloWorld"
X = int(input())

prefill = helloworld[: X - 1]
postfill = helloworld[X:]

result = prefill + postfill
print(result)
