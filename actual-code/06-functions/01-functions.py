# function
# func
# fn

# define

def some_meaningful_name(name: str, location="Geneva", team="HSE"):
    """
    This is a function prints hello.
    To use it, invoke passing the name as a string.
    :return:
    """
    print(f"Hello {name}! How is it in {location}? Is the work on {team} interesting?")


some_meaningful_name(name="Sally", team="LMF")
some_meaningful_name("Linh")
some_meaningful_name("Kevin", "Belfast", "training")

def generate_experiment(log_times = True, log_temperatures = True):
    ...

generate_experiment(log_temperatures=False)
