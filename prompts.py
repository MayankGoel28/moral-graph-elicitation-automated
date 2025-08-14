GIVE_MORAL_STANCE = "Given the above scenario, what is your moral stance? Please provide a brief explanation of your reasoning. Your output should be one of YTA (You're The Asshole), NTA (Not The Asshole), ESH (Everyone Sucks Here), or NAH (No Assholes Here), followed by a | and your reasoning. For example, 'YTA | I think you should have been more considerate of their feelings.'"

ANALOGOUS_SITUATIONS = "Think of 3 other scenarios, in different contexts and situations where the same moral principle you applied here would lead to the same judgment. Output 3 line separated situations. Don't add any introductory phrases or other texts."

STRESS_TEST_SITUATIONS = "Think of 3 other scenarios, in different contexts and situations where the same moral principle you applied here would lead to a different judgment. Output 3 line separated situations. Don't add any introductory phrases or other texts."

PAST_SITUATIONS = "Make a sci-fi, fantasy, historical or something weird - but a sitation about the same moral principle. Don't add any introductory phrases or other texts."

VALUE_CARD_GENERATION = '''Summarize the core moral value demonstrated across all these scenarios in JSON format:
{
  "value_name": "[Core principle]",
  "description": "[How this value guides decision-making]",
  "applications": "[Key contexts where this value applies]",
}
Don't add any introductory phrases or other texts.'''

def value_from_situations(situations_text):
    return f"""Below are several situations. All of them encode a specific moral stance. Based on the situations, find a common value that is shared or considered by all of them.\n\n{situations_text}\n\nWhat is the common value that is shared or considered by all of them?.
Follow the format in {VALUE_CARD_GENERATION}"""

def value_zeroshot(dilemma, moral_stance):
    return f"""Given the following dilemma and moral stance, generate a JSON object that summarizes the core moral value demonstrated in the situation and moral stance taken.\nDilemma: {dilemma}\nMoral Stance: {moral_stance}\n\n 
Follow the format in {VALUE_CARD_GENERATION}"""