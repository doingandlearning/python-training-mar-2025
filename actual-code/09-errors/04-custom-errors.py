# This is what everyone else does: class CERNError extends Exception:
class CERNError(Exception):
    pass

class NotTitleCaseError(Exception):
    pass



class ReadingError(Exception):
    def __init__(self, device_id, value):
        # super lets me interact with the parent class - super class
        super().__init__(f"There was an error with device {device_id} with a value {value}.")
        self.device_id = device_id
        self.value = value


try:
    # raise CERNError("Something went wrong")
    name = input("What's your name? ")
    if not name.istitle():
        raise NotTitleCaseError()
    print(f'Hi {name}!')
    raise ReadingError(7, 567)
except CERNError:
    print("We were responsible for this problem")
except NotTitleCaseError:
    print("Names should start with a capital letter")
except ReadingError as exp:
    if exp.device_id == 7:
        print("Oops! That's been faulty for a while!")
    print(exp)