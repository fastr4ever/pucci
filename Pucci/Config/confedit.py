def Conf():

    try:

        CreateChannels = input("Do you want to create channels? (y/n): ")

        if CreateChannels == "y":

            with open("CREATECHANNELS.bool", "w") as w:
                w.write("True")

            NumberOfChannels = input("Number of channels? (int): ")

            with open("NUMBEROFCHANNELS.integrer", "w") as w:
                w.write(NumberOfChannels)

            NameOfChannels = input("Name of channels? (str): ")

            with open("NAMEOFCHANNELS.string", "w") as w:
                w.write(NameOfChannels)

        elif CreateChannels == "n":

            with open("CREATECHANNELS.bool", "w") as w:
                w.write("False")

        CreateRoles = input("Do you want to create roles? (y/n): ")

        if CreateRoles == "y":

            with open("CREATEROLES.bool", "w") as w:
                w.write("True")

            RolesName = input("Roles names? (str): ")

            with open("ROLENAMES.string", "w") as w:
                w.write(RolesName)

        elif CreateRoles == "n":

            with open("CREATEROLES.bool", "w") as w:
                w.write("False")

        DeleteChannels = input("Do you want to delete channels? (y/n): ")

        if DeleteChannels == "y":

            with open("DELETECHANNELS.bool", "w") as w:
                w.write("True")

        elif DeleteChannels == "n":

            with open("DELETECHANNELS.bool", "w") as w:
                w.write("False")
    
    except KeyboardInterrupt:

        pass

Conf()