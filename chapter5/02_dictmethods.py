marks={"darss": 67,
       "harsh":56,
       "kalu":66
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"darss":98})
print(marks)
print(marks.get("darss"))


# Remove and return the value for key "harsh"
removed_value = marks.pop("harsh")
print("Removed value:", removed_value)   # Output: 56

print("Updated dictionary:", marks)
# Output: {'darss': 67, 'kalu': 66}
