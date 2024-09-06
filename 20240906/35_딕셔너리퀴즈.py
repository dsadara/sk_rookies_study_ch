data_dict = {
    "name":"John",
    "phone":"010-1234-5678",
    "email":"john@python.com",
    "birth":"112233"
    }

print(data_dict)

print(data_dict.get("name"))

data_dict["birth"] = "445566"
print(data_dict)

data_dict["city"] = "Seoul"
print(data_dict)