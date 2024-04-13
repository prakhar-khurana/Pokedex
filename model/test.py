import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

# Load the trained model
model = tf.keras.models.load_model('pokemon_recognition_model.h5')

# Define the target image size
target_size = (224, 224)

# Load and preprocess the input imag
input_image = load_img('test10.png', target_size=target_size)
input_array = img_to_array(input_image) / 255.0
input_array = np.expand_dims(input_array, axis=0)

# Make the prediction
predictions = model.predict(input_array)

# Get the list of Pokemon names from the directory
pokemon_names = ['Abra', 'Aerodactyl', 'Alakazam', 'Arbok', 
                 'Arcanine', 'Articuno', 'Beedrill', 'Bellsprout', 
                 'Blastoise', 'Bulbasaur', 'Butterfree', 'Caterpie', 
                 'Chansey', 'Charizard', 'Charmander', 'Charmeleon', 
                 'Clefable', 'Clefairy', 'Cloyster', 'Cubone', 
                 'Dewgong', 'Diglett', 'Ditto', 'Dodrio', 'Doduo', 
                 'Dragonair', 'Dragonite', 'Dratini', 'Drowzee', 
                 'Dugtrio', 'Eevee', 'Ekans', 'Electabuzz', 'Electrode', 
                 'Exeggcute', 'Exeggutor', 'Farfetchd', 'Fearow', 
                 'Flareon', 'Gastly', 'Gengar', 'Geodude', 'Gloom', 
                 'Golbat', 'Goldeen', 'Golduck', 'Golem', 'Graveler', 
                 'Grimer', 'Growlithe', 'Gyarados', 'Haunter', 
                 'Hitmonchan', 'Hitmonlee', 'Horsea', 'Hypno', 'Ivysaur', 
                 'Jigglypuff', 'Jolteon', 'Jynx', 'Kabuto', 'Kabutops', 
                 'Kadabra', 'Kakuna', 'Kangaskhan', 'Kingler', 'Koffing', 
                 'Krabby', 'Lapras', 'Lickitung', 'Machamp', 'Machoke', 
                 'Machop', 'Magikarp', 'Magmar', 'Magnemite', 'Magneton', 
                 'Mankey', 'Marowak', 'Meowth', 'Metapod', 'Mew', 
                 'Mewtwo', 'Moltres', 'MrMime', 'Muk', 'Nidoking', 
                 'Nidoqueen', 'Nidorina', 'Nidorino', 'Ninetales', 
                 'Oddish', 'Omanyte', 'Omastar', 'Onix', 'Paras', 
                 'Parasect', 'Persian', 'Pidgeot', 'Pidgeotto', 'Pidgey', 
                 'Pikachu', 'Pinsir', 'Poliwag', 'Poliwhirl', 'Poliwrath', 
                 'Ponyta', 'Porygon', 'Primeape', 'Psyduck', 'Raichu', 
                 'Rapidash', 'Raticate', 'Rattata', 'Rhydon', 'Rhyhorn', 
                 'Sandshrew', 'Sandslash', 'Scyther', 'Seadra', 'Seaking', 
                 'Seel', 'Shellder', 'Slowbro', 'Slowpoke', 'Snorlax', 
                 'Spearow', 'Squirtle', 'Starmie', 'Staryu', 'Tangela', 
                 'Tauros', 'Tentacool', 'Tentacruel', 'Vaporeon', 
                 'Venomoth', 'Venonat', 'Venusaur', 'Victreebel', 
                 'Vileplume', 'Voltorb', 'Vulpix', 'Wartortle', 'Weedle', 
                 'Weepinbell', 'Weezing', 'Wigglytuff', 'Zapdos', 'Zubat']

# Get the top 3 predictions
top_3_indices = np.argsort(predictions[0])[-3:][::-1]
top_3_probabilities = [predictions[0][i] for i in top_3_indices]
top_3_pokemon = [pokemon_names[i] for i in top_3_indices]

# Print the results
print("Top 3 Predicted Pokemon:")
for i in range(3):
    print(f"{i+1}. Pokemon: {top_3_pokemon[i]}, Probability: {top_3_probabilities[i]:.2f}")