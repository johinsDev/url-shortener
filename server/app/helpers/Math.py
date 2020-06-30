from math import floor


class Math():
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    @classmethod
    def encode_id(cls, value, b=62):
        r = value % b

        result = cls.ALPHABET[r]

        q = floor(value / b)

        while(q):
            r = q % b
            q = floor(q / b)

            result = cls.ALPHABET[r] + result

        return result
