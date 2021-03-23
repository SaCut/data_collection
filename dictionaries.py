# dictinoaries

sparta_students = {
	"Key": "Value",
	"First name": "Eddie",
	"Last name": "Murphy",
	"Stream": "DevOps",
	"completed lessons": 3,
	"topics": ["variables", "data types", "collections"]
}

# print(sparta_students)


# # retrieve the data type from the value of a key
# print(type(sparta_students["topics"]))

# # retrieve a data type from a dictionary through indexing
# print(type(sparta_students["topics"][1]))

# # get back all the keys in a dictionary
# print(sparta_students.keys())

# add "operators" to the topics
sparta_students["topics"].append("operators")

# change the completed lessons from 3 to 4
sparta_students["completed lessons"] = 4

# remove "data type" from "topics"
sparta_students["topics"].remove("data types")

# checking again
print(sparta_students)