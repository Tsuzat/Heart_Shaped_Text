# defining a function which prints love shapes text
def love(text:str):
    n = len(text) #length of the text
    print(
        "\n".join(
            [
                "".join(
                    [
                        (
                            text[(x-y)%n]
                            if ((x*0.05)**2 + (y*0.1)**2 -1)**3
                            - (x*0.05)**2 * (y*0.1)**3
                            <= 0
                            else " "
                        )
                        for x in range(-30,30)
                    ]
                )
                for y in range(15,-15,-1)
            ]
        )
    )

if __name__ == "__main__":
    love(input("Input text: "))