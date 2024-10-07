import pickle
import base64

serialized = input('enter the serialized string: ')

#TO-DO detect if the serialised object is encoded in any way and on that basis decode it.

decoded_data = base64.b64decode(serialized)

deserialized = pickle.loads(decoded_data)

try:
    deserialized = pickle.loads(decoded_data)
    print("Deserialización exitosa:", deserialized)

except AttributeError as e:
    print(f"Error: Falta la clase necesaria para la deserialización: {e}")

except Exception as e:
    print(f"Error durante la deserialización: {e}")
