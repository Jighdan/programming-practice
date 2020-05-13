# Script flow 

1. Fetch words and organize them in a list

2. Pick a random word from the list and display it with it's characters hidden
```
display_format = {
	"secret_word": "example",
	"hidden_word": "_ _ _ _ _ _ _"}
```
2.5 Filter the user input:
	> Is it a string?
	> Is it just ONE character

3. Guessing a letter
- Rules:
	- Can't re-input the same word
- Logic
	if: lives greater or equal 1 =>
		else if: the letter exists in the secret word => 
			set the "hidden word" to display such changes

			if: "hidden_word" is completed =>
				end program

		else: letter is not present in word => 
			take a life out

4. Syntaxes
>>> [list.index(n)] only displays first occurence of an item 
		(CHECK for duplicates)

