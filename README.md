# Twenty Questions AI Agents

An experiment with two LLM agents playing Twenty Questions against each other.

Each agent has their own secret system instructions that aren't shared with the other.

The guessing agent doesn't know what the answer is, but will try to guess it by asking questions.

When using a strong model like GPT-4 it often succeeds in finding the answer.

## Example Game Run:

```
User Input: What object should the guesser try to guess?
banana

Guesser: Is it a living thing?
Asker: No
Guesser: Is it something you can hold in your hand?
Asker: Yes
Guesser: Is it made of metal?
Asker: No
Guesser: Is it used in day-to-day life?
Asker: Yes
Guesser: Is it electronic?
Asker: No
Guesser: Is it made of plastic?
Asker: No
Guesser: Is it associated with a specific room in the house?
Asker: No
Guesser: Is it something that you can write or draw with?
Asker: No
Guesser: Is it something you wear?
Asker: No
Guesser: Is it something you can consume, such as food or drink?
Asker: Yes
Guesser: Is it a type of beverage?
Asker: No
Guesser: Is it sweet?
Asker: Yes
Guesser: Is it a type of fruit?
Asker: Yes
Guesser: Is it typically red when ripe?
Asker: No
Guesser: Is it typically eaten peeled?
Asker: Yes
Guesser: Is it tropical fruit?
Asker: Yes
Guesser: Is it a banana?
Asker: Yes, you got it! It is a banana! Congratulations!
Guesser: Awesome! That was fun, thank you!
```
