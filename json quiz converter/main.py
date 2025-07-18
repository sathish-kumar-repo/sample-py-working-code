import json

# Load from file
with open("questions.json", "r") as f:
    old_questions = json.load(f)


def convert_questions(old_list):
    new_list = []
    for idx, item in enumerate(old_list, start=1):
        options = [item[letter] for letter in ("A", "B", "C", "D")]
        correct_idx = ord(item["answer"]) - ord("A")
        new_list.append(
            {
                "id": idx,
                "question": item["question"],
                "options": options,
                "correctAnswer": correct_idx,
            }
        )
    return new_list


# Convert and optionally write to new JSON file
new_questions = convert_questions(old_questions)

with open("converted_questions.json", "w") as f:
    json.dump(new_questions, f, indent=2)

print("Converted questions saved to converted_questions.json")
