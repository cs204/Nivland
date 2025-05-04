hello = input('Приветствие: ').strip().lower()
if hello.startswith("здравствуйте"):
    print("$0")
elif hello.startswith(('з')) and not hello.startswith(("здравствуйте")):
    print("$20")
else:
    print("$100")
