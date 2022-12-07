#!/user/bin/env.python3
# Created By: Jeremiah omoike
# Date: Dec 6, 2022
# This program creates a canadian mailing address using user inputs


def format_address(
    name, question, street_num, street_name, city, province, postal_code, apt_num=None
):
    # format strings and sets them as uppercase
    address = (
        name.upper()
        + "\n"
        + street_num
        + " "
        + street_name.upper()
        + "\n"
        + city.upper()
        + " "
        + province.upper()
        + " "
        + postal_code.upper()
    )
    # if user lives in an apartment it adds apartment number
    if question == "y":
        can_post_address = (
            name.upper()
            + "\n"
            + apt_num
            + "-"
            + street_num
            + " "
            + street_name.upper()
            + "\n"
            + city.upper()
            + " "
            + province.upper()
            + " "
            + postal_code.upper()
        )
        return can_post_address
    return address


# gets input from user and displays the address
def main():
    apt_num_user = None

    print("This program creates an address to a Canadian mailing address")
    print("")

    # gets input from the user
    full_name_user = input("Enter your full name: ")
    q_about_user = input("Do you live in an apartment? (y/n): ")

    # check if user lives in an apartment
    if q_about_user == "y":
        apt_num_user = input("Enter your apartment number: ")

    # gets inputs from the user
    street_num_user = input("Enter your street number: ")
    street_name_user = input(
        "Enter your street name and " "type (Main St., Windsor ave., etc.): "
    )
    city_user = input("What is the name of your city?: ")
    province_user = input(
        "Enter your province (as an abbreviation " "i.e ON, AB, etc.): "
    )
    postal_user = input("Enter your postal code (i.e A1B3y3 2C3B21): ")

    # assigns varaible to the function that formats the address
    if apt_num_user is not None:
        user_address = format_address(
            full_name_user,
            q_about_user,
            street_num_user,
            street_name_user,
            city_user,
            province_user,
            postal_user,
            apt_num_user,
        )
    else:
        user_address = format_address(
            full_name_user,
            q_about_user,
            street_num_user,
            street_name_user,
            city_user,
            province_user,
            postal_user,
        )
    print("")
    print("This is your Canadian mailing address:\n")
    print(user_address)


if __name__ == "__main__":
    main()
