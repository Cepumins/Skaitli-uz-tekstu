
number_to_text = {
    0: "nulle",
    1: "viens",
    2: "divi",
    3: "trīs",
    4: "četri",
    5: "pieci",
    6: "seši",
    7: "septiņi",
    8: "astoņi",
    9: "deviņi",
    10: "desmit",
    11: "vienpadsmit",
    12: "divpadsmit",
    13: "trīspadsmit",
    14: "četrpadsmit",
    15: "piecpadsmit",
    16: "sešpadsmit",
    17: "septiņpadsmit",
    18: "astoņpadsmit",
    19: "deviņpadsmit",
    20: "divdesmit",
    30: "trīsdesmit",
    40: "četrdesmit",
    50: "piecdesmit",
    60: "sešdesmit",
    70: "septiņdesmit",
    80: "astoņdesmit",
    90: "deviņdesmit",
    100: "simts"
}

thousand_separators = ["", "tūkstoši", "miljoni", "miljardi", "triljoni"]
one_thousand_separators = ["", "tūkstotis", "miljons", "miljards", "triljons"]

def get_whole_number():
    while True:
        try:
            user_input = int(input("Ievadiet veselu numuru: "))
            return user_input
        except ValueError:
            print("Šis nav vesels numurs, mēģiniet vēlreiz.")

def number_to_words(number):
    if number == 0:
        return "nulle"

    words = []

    is_negative = number < 0
    if is_negative:
        number = abs(number)

    # Process each chunk of 3 digits
    chunk_count = 0
    while number > 0:
        chunk = number % 1000
        if chunk > 0:
            words_chunk = []

            hundreds_digit = chunk // 100
            if hundreds_digit > 0:
                if hundreds_digit == 1:
                    words_chunk.append("simts")
                else:
                    words_chunk.append(number_to_text[hundreds_digit] + " simti")
                chunk %= 100

            if chunk >= 20:
                words_chunk.append(number_to_text[chunk - chunk % 10])
                chunk %= 10

            if chunk > 0:
                words_chunk.append(number_to_text[chunk])

            # Determine which thousand separator to use
            if chunk_count == 1 and chunk == 1:
                separator = one_thousand_separators[chunk_count]
            else:
                separator = thousand_separators[chunk_count]

            words.append(" ".join(words_chunk) + " " + separator)

        number //= 1000
        chunk_count += 1

    words = " ".join(reversed(words)).strip()

    if is_negative:
        words = "mīnus " + words

    return words

def process_number():
    number = get_whole_number()
    print(f"Jūs ievadījāt: {number:,}")

    # Convert the number to words
    words = number_to_words(number)
    print(f"Numurs vārdos: {words}")

process_number()
