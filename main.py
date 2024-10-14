##### Handle exceptions

def main():
    try:
        open("/path/to/mars.jpg")
    except FileNotFoundError:
        print("Coldn't find the config.txt")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except Exception as e:
        print(type(e))
    finally:
        print("Todo correcto")
            

main()

