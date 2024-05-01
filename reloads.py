# import sample
# import sample
# import sample
# import sample


# reload funtion


# import importlib
# import sample

# importlib.reload(sample)
# importlib.reload(sample)
# importlib.reload(sample)
# importlib.reload(sample)

# another method 

import importlib
import filechanges

def changes():
    try:
        importlib.reload(filechanges)
        filechanges.print_changes()

    except:
        pass

for i in range(5):
    changes()
    input("hint to enter reload funtion")