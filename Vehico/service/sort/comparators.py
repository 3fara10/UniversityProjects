
from domain.masina import Masina


# -----------------------------complex comparators
def marca_model_comparator(masina1: Masina, masina2: Masina):
    """
        Compares two Masina objects first by brand and then by model.

        Parameters:
            masina1 (Masina): The first Masina object to compare.
            masina2 (Masina): The second Masina object to compare.

        Returns:
            int: -1 if masina1 comes before masina2, 1 if masina1 comes after masina2, 0 if they are equal in terms of brand and model.
    """
    # First, compare by brand
    if generic_comparator('_marca')(masina1, masina2) != 0:
        return generic_comparator('_marca')(masina1, masina2)
    else:
        # If marca are the same, compare by model
        return generic_comparator('_model')(masina1, masina2)


def marca_model_token_comparator(masina1: Masina, masina2: Masina):
    """
        Compares two Masina objects first by brand, then by model, and finally by token.

        Parameters:
            masina1 (Masina): The first Masina object to compare.
            masina2 (Masina): The second Masina object to compare.

        Returns:
            int: -1 if masina1 comes before masina2, 1 if masina1 comes after masina2, 0 if they are equal in terms of brand, model, and token.
    """
    # First, compare by marca
    if generic_comparator('_marca')(masina1, masina2) != 0:
        return generic_comparator('_marca')(masina1, masina2)
    else:
        # If marca are the same, compare by model
        if generic_comparator('_model')(masina1, masina2) != 0:
            return generic_comparator('_model')(masina1, masina2)
        else:
            # If model are the same, compare by token
            return generic_comparator('_tokenMasina')(masina1, masina2)


# ------------------------------------basic comparators
def generic_comparator(attribute: str):
    """
       Creates a comparator function for a specified attribute of Masina.

       Parameters:
           attribute (str): The attribute of Masina to compare.

       Returns:
           A comparator function that compares two Masina objects based on the specified attribute.
       """
    return lambda obj1, obj2: (
        -1 if getattr(obj1, attribute) < getattr(obj2, attribute)
        else 1 if getattr(obj1, attribute) > getattr(obj2, attribute)
        else 0)



