def log_and_run(func):
    print("About to test function ...")
    func()
    print("Just tested function ...")

log_and_run(lambda: print("I am a function under test."))