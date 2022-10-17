def greeting(name):
 print(f"Hi {name}")

greeting("TOMAS")

def get_greeting(name):
 return f"Hi {name}"


message = get_greeting("ashley")
file = open("context.txt", "w")
file.write(message)