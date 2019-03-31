# Strand
Strand allows you to randomly generate text for use in programs, games, or just for fun.
## Usage
To start using Strand, use `import strand` at the beginning of your Python code. To parse Strand text, use `strand.parse()` and pass in the text to parse.

Strand text can contain normal text as well as random choices of text contained within square brackets `[]`. Inside of square brackets, you can put multiple different pieces of text separated by vertical pipes `|` and Strand will randomly choose one of them.

Example: `I have a [cat|dog]` outputs either "I have a cat" or "I have a dog"

Choices can be nested, in which case they will only be evaluated if the surrounding option is chosen

Example: `I have a [[good|bad] cat|dog]` outputs either "I have a good cat", "I have a bad cat", or "I have a dog"
