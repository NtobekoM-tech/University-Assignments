#Program to determine the type of animal based on a classification scheme
#Ntobeko Mhlongo
#05-03-2024

print("Welcome to the Biology Expert")
print("-----------------------------")
print("Answer the following questions by selecting from among the options.")

skeleton = str(input("The skeleton is (internal/external)?\n"))


if skeleton == "external":#code for external skeleton
    print("Type of animal: Arthropod")

elif fertilisation := str(input("The fertilisation of eggs occurs (within the body/outside the body)?\n")):#code for internal skeleton

    if fertilisation == "within the body":#code for fertilisation within the body
        young = str(input("Young are produced by (waterproof eggs/live birth)?\n"))

        if young == "waterproof eggs":#code for young produced by waterproof eggs
            skin = str(input("The skin is covered by (scales/feathers)?\n"))

            if skin == "scales":#code scale covered skin
                print("Type of animal: Reptile")

            else:#code feather covered skin
                print("Type of animal: Bird")

        else:#code for young produced by live birth
            print("Type of animal: Mammal")

    elif fertilisation == "outside the body":#code for fertilisation outside the body
        lives = str(input("It lives (in water/near water)?\n"))

        if lives == "in water":#code for animal living in water
            print("Type of animal: Fish")

        else:#code for animal living near water
            print("Type of animal: Amphibian")