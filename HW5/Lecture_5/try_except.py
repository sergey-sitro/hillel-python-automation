some_variable
1/0
"str" + 1

try:
	print(some_variable)
except NameError:
	print("Something went wrong")


try:
	print(some_variable)
except NameError as e:
	print("Something went wrong")
	raise e

try:
	print(1/0)
except NameError as e:
	print("Something went wrong")
	raise e

try:
	print(1/0)
except NameError as e:
	print("Something went wrong")
	raise e
except ZeroDivisionError as e:
	print("boom!")
	raise e

try:
	print(1/0)
except (NameError, ZeroDivisionError) as e:
	print("Something went wrong")
except ZeroDivisionError as e:
	print("boom!")


try:
	print("Do not divide by zero")
except NameError as e:
	print("Something went wrong")
	raise e
except ZeroDivisionError as e:
	print("boom!")
	raise e
else:
	print("Seems like all is ok")


try:
	print(1/0)
except NameError as e:
	print("Something went wrong")
	raise e
except ZeroDivisionError as e:
	print("boom!")
	raise e
else:
	print("Seems like all is ok")


try:
	print(1/0)
except NameError as e:
	print("Something went wrong")
	raise e
except ZeroDivisionError as e:
	print("boom!")
	raise e
else:
	print("Seems like all is ok")
finally:
	print("I have the final word")


try:
	print("Do not divide by zero")
except NameError as e:
	print("Something went wrong")
	raise e
except ZeroDivisionError as e:
	print("boom!")
	raise e
else:
	print("Seems like all is ok")
finally:
	print("I have the final word")


try:
	some_variable
finally:
	print("finally")


try:
	some_variable
except:
	pass

try:
	some_variable
except Exception:
	pass
