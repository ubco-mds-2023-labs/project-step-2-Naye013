import numpy as np

class EntityProcessor:
    """
    A class for processing and analyzing entities with key-value characteristics.
    """

    def __init__(self):
        """
        Initialize an EntityProcessor instance.
        """
        self.entities = {}

    def entity(self, entity_id, characteristics):
        """
        Process an individual entity and store its characteristics.

        Parameters:
        - entity_id (str): The ID or label of the entity.
        - characteristics (dict): Key-value pairs representing the characteristics of the entity.
        """
        if entity_id not in self.entities:
            self.entities[entity_id] = {}

        for key, value in characteristics.items():
            self.entities[entity_id][key] = value

    def entity_collection(self, entity_processor, entity_id):
        """
        Process an entity and add its values to the entity collection.

        Parameters:
        - entity_processor (EntityProcessor): An instance of EntityProcessor containing entity data.
        - entity_id (str): The ID or label of the entity to process.
        """
        entity_data = entity_processor.get_entity(entity_id)

        if entity_data:
            for key, value in entity_data.items():
                if key not in self.entities:
                    self.entities[key] = []

                # Convert values to a common numeric type if they are not already
                if isinstance(value, (int, float, np.number)):
                    self.entities[key].append(value)
                elif isinstance(value, str) and value.isnumeric():
                    self.entities[key].append(float(value))
                else:
                    print(f"Skipping value for key '{key}' as it is not numeric.")

    def get_entity(self, entity_id):
        """
        Retrieve the characteristics of a specific entity.

        Parameters:
        - entity_id (str): The ID or label of the entity to retrieve.

        Returns:
        - dict or None: A dictionary containing the characteristics of the entity, or None if not found.
        """
        return self.entities.get(entity_id, None)

    def compute_basic_statistics(self, key):
        """
        Compute the mean of the values associated with a specific key in the entity collection.

        Parameters:
        - key (str): The key for which to compute the mean.

        Returns:
        - float or None: The mean of the values associated with the key, or None if no values are found.
        """
        values = self.entities.get(key, [])

        if values:
            mymean = np.mean(values)
            return mymean
        else:
            return None


    #def compute_basic_statistics(self, data):
    #    mymean = np.mean(data)
    #    mymedian = np.median(data)
    #    mysd = np.std(data)
    #    mymode = mode(data)
    #    mymin = min(data)
    #    mymax = max(data)
    #    mycount = len(data)
