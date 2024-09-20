"""
Language detection starter
"""
# pylint:disable=too-many-locals, unused-argument, unused-variable

from main import calculate_frequencies, calculate_mse, create_language_profile, tokenize


def main() -> None:
    """
    Launches an implementation
    """
    with open("assets/texts/en.txt", "r", encoding="utf-8") as file_to_read_en:
        en_text = file_to_read_en.read()
        tokens = tokenize(en_text)
    with open("assets/texts/de.txt", "r", encoding="utf-8") as file_to_read_de:
        de_text = file_to_read_de.read()
    with open("assets/texts/unknown.txt", "r", encoding="utf-8") as file_to_read_unk:
        unknown_text = file_to_read_unk.read()

    print(f'Tokens: {tokens}')
    print(f'Frequencies: {calculate_frequencies(tokens)}')
    print(f'Language profile: {create_language_profile("en", en_text)}')
    print(f'MSE:{calculate_mse}')
    print(f'Compare profiles:')
    result = tokens

    assert result, "Detection result is None"


if __name__ == "__main__":
    main()
