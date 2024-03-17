# Twenty Questions AI Agents

An experiment with two LLM agents playing Twenty Questions against each other.

Each agent has their own secret system instructions that aren't shared with the other.

The guessing agent doesn't know what the answer is, but will try to guess it by asking questions.

When using a strong model like GPT-4 it often succeeds in finding the answer.

## Example Game Run:

There are more examples located in the `examples` directory.

```
What thing would you like Knower to be thinking of?
the magic schoolbus

Knower: I'm thinking of something. Ask me questions to figure out what it is. Here is a riddle:

"On this fantastical ride, classroom rules slide.
Fear not where you'll wind up, for it's an educational trip.
No highway, sea, or sky is too wide,
All aboard, let's give logic the slip."

Guesser: Is it something that could be found in a classroom?

Knower: Yes

Guesser: Is it a tangible object?

Knower: Yes

Guesser: Is this object related to literature or books?

Knower: Yes

Guesser: Is it a specific book?

Knower: Yes

Guesser: Is this book typically read by children?

Knower: Yes

Guesser: Does the book contain illustrations?

Knower: Yes

Guesser: Is the book part of a series?

Knower: Yes

Guesser: Is the setting of this book in a magical or unordinary world?

Knower: Yes

Guesser: Is the main character of this book a child?

Knower: No

Guesser: Is the author of the book American?

Knower: Yes

Guesser: Is the main character of this book a fictional creature or animal?

Knower: No

Guesser: Is the book written by Dr. Seuss?

Knower: No

Guesser: Is the book published before the 1960s?

Knower: No

Guesser: Is the book primarily educational in nature, teaching kids about different subjects or concepts?

Knower: Yes

Guesser: Is the book associated with a TV show or has it been adapted into a TV show?

Knower: Yes

Guesser: Is the book "The Magic School Bus"?

Knower: Yes

Guesser: So, it's definitely "The Magic School Bus". This series expands children's imaginations and knowledge by transforming an ordinary school bus into a magical vehicle that can go anywhere and do anything, which ties perfectly with your riddle!

Knower: Yes, spot on! It is indeed "The Magic School Bus". Great job on the series of questions!

Guesser: Thank you! I'm so glad I could guess it right. It was an interesting and challenging task, as the Magic School Bus is a unique blend of fantasy and education. Thank you for the fun game!
```
