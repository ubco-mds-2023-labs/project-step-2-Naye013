import numpy as np
from scipy.stats import mode

class Entity:
    def __init__(self, entity_id, field_value_pairs):
        """
        Initialize an Entity instance.

        Parameters:
        - entity_id (str): The ID or label of the entity.
        - field_value_pairs (dict): Key-value pairs representing the characteristics of the entity.
        """
        self.entity_id = entity_id
        self.field_value_pairs = self.validate_and_convert(field_value_pairs)

    def validate_and_convert(self, field_value_pairs):
        """
        Validate and convert values to a common numeric type if they are not already.

        Parameters:
        - field_value_pairs (dict): Key-value pairs representing the characteristics of the entity.

        Returns:
        - dict: Validated key-value pairs.
        """
        validated_pairs = {}
        for field, value in field_value_pairs.items():
            try:
                validated_value = float(value)
            except (ValueError, TypeError):
                print(f"Skipping value for field '{field}' in entity '{self.entity_id}' as it is not numeric.")
                continue
            validated_pairs[field] = validated_value
        return validated_pairs

class EntityCollection:
    def __init__(self, items=None):
        """
        Initialize an EntityCollection instance.

        Parameters:
        - items (list): List of Entity instances (optional).
        """
        self.items = items or []

    def add(self, entity_id, field_values):
        """
        Add an entity to the collection.

        Parameters:
        - entity_id (str): The ID or label of the entity.
        - field_values (dict): Key-value pairs representing the characteristics of the entity.
        """
        new_entity = Entity(entity_id, field_values)
        self.items.append(new_entity)

    def compute_mean(self, key):
        """
        Compute the mean of the values associated with a specific key across all entities.

        Parameters:
        - key (str): The key for which to compute the mean.

        Returns:
        - float or None: The mean of the values associated with the key, or None if no values are found.
        """
        values = self._get_values_for_key(key)
        return np.mean(values) if values else None

    def compute_mode(self, key):
        """
        Compute the mode of the values associated with a specific key across all entities.

        Parameters:
        - key (str): The key for which to compute the mode.

        Returns:
        - float or None: The mode of the values associated with the key, or None if no values are found.
        """
        values = self._get_values_for_key(key)
        return mode(values).mode[0] if values else None

    def compute_median(self, key):
        """
        Compute the median of the values associated with a specific key across all entities.

        Parameters:
        - key (str): The key for which to compute the median.

        Returns:
        - float or None: The median of the values associated with the key, or None if no values are found.
        """
        values = self._get_values_for_key(key)
        return np.median(values) if values else None

    def compute_min(self, key):
        """
        Compute the minimum of the values associated with a specific key across all entities.

        Parameters:
        - key (str): The key for which to compute the minimum.

        Returns:
        - float or None: The minimum of the values associated with the key, or None if no values are found.
        """
        values = self._get_values_for_key(key)
        return min(values) if values else None

    def compute_max(self, key):
        """
        Compute the maximum of the values associated with a specific key across all entities.

        Parameters:
        - key (str): The key for which to compute the maximum.

        Returns:
        - float or None: The maximum of the values associated with the key, or None if no values are found.
        """
        values = self._get_values_for_key(key)
        return max(values) if values else None

    def compute_count(self, key):
        """
        Compute the count of the values associated with a specific key across all entities.

        Parameters:
        - key (str): The key for which to compute the count.

        Returns:
        - int or None: The count of the values associated with the key, or None if no values are found.
        """
        values = self._get_values_for_key(key)
        return len(values) if values else None

    def _get_values_for_key(self, key):
        """
        Get the values associated with a specific key across all entities.

        Parameters:
        - key (str): The key for which to retrieve the values.

        Returns:
        - list: List of values associated with the key.
        """
        values = [entity.field_value_pairs.get(key, None) for entity in self.items]
        return [value for value in values if value is not None]
