import json
John =         {
            "firstName": "John",
            "age": 1
        }
with open("Example.json") as file_ctx:
    lines = file_ctx.read()
    source_data = json.loads(lines)
    print(source_data["firstName"])
#source_data["hobbies"].append["drawing"]
source_data["children"].append(John)
with open("Example.json","w") as file_ctx:
    json.dump(source_data,file_ctx,indent=4)

