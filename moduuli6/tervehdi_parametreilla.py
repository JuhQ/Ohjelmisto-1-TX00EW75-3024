def tervehdi(kerrat, tervehdys):
    for i in range(kerrat):
        print(str(tervehdys) + " " + str(i + 1) + " times")
        print(f"{tervehdys} {i + 1} times")

tervehdi(2, "hello")
print("----")
tervehdi(3, "moikka")