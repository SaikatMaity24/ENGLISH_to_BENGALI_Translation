import pandas as pd
import re


def separate_languages(text):
    if not isinstance(text, str):  # Check if text is a string
        return None, None

    parts = text.split('//')

    if len(parts) != 2:
        return None, None

    english = parts[0].strip()
    bangla = parts[1].strip()

    if not all(ord(char) < 128 for char in english):
        return None, None

    if not any(ord(char) >= 128 for char in bangla):
        return None, None

    return english, bangla


# Read the CSV file
df = pd.read_csv(r'C:\Dev\CODES\python\INTERNSHIP_WEBEL\Anubad\ONUBAD.csv')

# Create empty lists to store separated sentences
english_sentences = []
bangla_sentences = []

# Process each row in the 'Responses' column
for response in df['Responses']:
    english, bangla = separate_languages(response)
    english_sentences.append(english)
    bangla_sentences.append(bangla)

# Create a new DataFrame with separated sentences
result_df = pd.DataFrame({
    'English': english_sentences,
    'Bangla': bangla_sentences
})

# Display the first few rows of the new DataFrame
print(result_df.head())

# Optionally, save the new DataFrame to a CSV file
result_df.to_csv('separated_sentences.csv', index=False)
result_df.to_excel("ujubuju.xlsx", index=False)
