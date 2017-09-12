test_dict = {}
test_dict["a"] = []
test_dict["a"].append("1")
print(id(test_dict["a"]))
test_dict["a"].append("2")
print(id(test_dict["a"]))
test_dict["a"].append("3")
print(id(test_dict["a"]))

print(test_dict)
