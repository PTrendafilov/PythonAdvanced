#Exercise: Stacks, Queues, Tuples, and Sets
This exercise provides a set of programming problems that aim to improve your skills in working with data structures like stacks, queues, tuples, and sets in Python. The problems are designed to challenge your understanding of these data structures and their practical application. You are expected to implement solutions and submit them through the SoftUni judge system.

##Problem 1: Numbers
Your task is to manipulate two sequences of integer values, perform various operations on them, and determine if one sequence is a subset of the other. You will be given commands to add or remove elements from the sequences, and you should implement these operations accordingly.

###Input:
Two sequences of integers values on different lines, separated by a space.
A number N, followed by N lines containing one of the following commands:
"Add First {numbers, separated by a space}"
"Add Second {numbers, separated by a space}"
"Remove First {numbers, separated by a space}"
"Remove Second {numbers, separated by a space}"
"Check Subset"

###Output:
For the "Check Subset" command, print "True" if any of the given sequences is a subset of the other, otherwise print "False".
In the end, print the final sequences, separated by a comma and a space ", ". The values in each sequence should be sorted in ascending order.

##Problem 2: Expression Evaluator
Write a program that evaluates a string expression given in the form of numbers and operators separated by a single space. Follow a simple rule: when encountering an operator, take all the numbers encountered so far, apply the operation, and save the result.

###Input:
A single line containing a string of integers and operators.

###Output:
A single number representing the result after the evaluation.

###Constraints:
The string will always end with an operator, resulting in one number as the result.
Valid operators are "*", "+", "-", and "/".
There will be no division by zero.
Negative numbers may appear in the string.

##Problem 3: Milkshakes
Learn how to make milkshakes by manipulating two sequences of integers representing chocolates and cups of milk. Your task is to match the chocolates with the cups of milk and prepare milkshakes according to the given rules.

###Input:
Two lines of input containing the integers representing the chocolates and the cups of milk, separated by ", ".

###Output:
If you successfully made 5 milkshakes: "Great! You made all the chocolate milkshakes needed!"
Otherwise: "Not enough milkshakes."
If there are chocolates left: "Chocolate: {chocolate1}, {chocolate2}, (…)"
If there are cups of milk left: "Milk: {milk1}, {milk2}, {milk3}, (…)"

###Constraints:
All given numbers will be valid integers in the range [-100 … 100].

##Problem 4: Honey
Worker-bees collect nectar. When a worker-bee has found enough nectar, she returns to the hive to drop off the load and pass the nectar to waiting bees so they can really start the honey-making process. 
You will receive 3 sequences:
a sequence of integers, representing working bees
a sequence of integers, representing nectar
a sequence of symbols – "+", "-", "*" or "/", representing the honey-making process.
Your task is to check if the bee has collected enough nectar to return to the hive and keep track of the total honey waiting bees made with the collected nectar.
Step one: check if a bee has collected enough nectar. You should take the first bee and try to match it with the last nectar:
If the nectar value is more or equal to the value of the bee, it is considered collected, and the bee returns to the hive to drop off the load (step two).
If the nectar value is less than the value of the bee, you should remove the nectar and try to match the bee with the next nectar's value until the bee collects enough nectar.
Step two: When a bee successfully collects nectar, she returns to the hive, and you should calculate the honey made. Take the first symbol in the sequence of symbols ("+", "-", "*" or "/") and make the corresponding calculation:
"{matched_bee} {symbol} {matched_nectar}"
The result represents the honey that is made from the passed nectar. The calculation should always return the absolute value of the result. After the calculation, remove the bee, the nectar, and the symbol.
Stop making honey when you are out of bees or nectar.


###Input:
On the first line, you will be given the values of bees - integers, separated by a single space
On the second line, you will be given the nectar's values - integers, separated by a single space
On the third line, you will be given symbols - "+", "-", "*" or "/", separated by a single space

###Output:
On the first line - print the total honey made:
"Total honey made: {total honey}"
On the next two lines print the bees or the nectar that are left, if there are any, otherwise skip the line:
"Bees left: {bee1}, {bee2}, … {beeN}"
"Nectar left: {nectar1}, {nectar2}, … {nectarN}"

###Constraints
All the bee's values will be integers in the range [0, 150]
Nectar's values will be integers in the range [0, 150]
There always will be enough symbols in the sequence of symbols

##Problem 5: Santa's Present Factory
This year Santa has decided to share his secret with you. Get ready to learn how his elves craft all the presents.
First, you will receive a sequence of integers representing the number of materials for crafting toys in one box. After that, you will be given another sequence of integers – their magic level.
Your task is to mix materials with magic so you can craft presents, listed in the table below with the exact magic level:


###Present	Magic needed
Doll	150
Wooden train	250
Teddy bear	300
Bicycle 	400

You should take the last box with materials and the first magic level value to craft a toy. Their multiplication calculates the total magic level. If the result equals one of the levels described in the table above, you craft the present and remove both materials and magic value. Otherwise:
If the product of the operation is a negative number, you should sum the values together, remove them both from their positions, and add the result to the materials.
If the product doesn't equal one of the magic levels in the table and is a positive number, remove only the magic value and increase the material value by 15.
If the magic or material (or both) equals 0, remove it (or both) and continue crafting the presents.
Stop crafting presents when you run out of boxes of materials or magic level values.
Your task is considered done if you manage to craft either one of the pairs:
a doll and a train
a teddy bear and a bicycle
###Input
The first line of input will represent the values of boxes with materials - integers, separated by a single space
On the second line, you will be given the magic values - integers again, separated by a single space
###Output
On the first line - print whether you've succeeded in crafting the presents:
"The presents are crafted! Merry Christmas!"
"No presents this Christmas!"
On the next two lines print the materials and magic that are left, if there are any (otherwise skip the line)
"Materials left: {material_N}, {material_N-1}, … {material_1}"
"Magic left: {magicValue_1}, {magicValue_2}, … {magicValue_N}"
On the next lines print the presents you have crafted, ordered alphabetically in the format:
"{toy_name1}: {amount}
{toy_name2}: {amount}
...
{toy_nameN}: {amount}"
###Constraints
All the materials' values will be integers in the range [1, 100]
Magic level values will be integers in the range [-10, 100]
In all cases, at least one present will be crafted

##Problem 6: Paint Colors
You will have to find all possible color combinations that can be used.
Write a program that finds colors in a string. You will be given a string on a single line containing substrings (separated by a single space) from which you will be able to form the following colors: 
Main colors: "red", "yellow", "blue"
Secondary colors: "orange", "purple", "green"
To form a color, you should concatenate the first and the last substrings and check if you can get any of the above colors' names. If there is only one substring left, you should use it to do the same check.
You can only keep a secondary color if the two main colors needed for its creation could be formed from the given substrings:
orange = red + yellow
purple = red + blue
green = yellow + blue
Note: You could find some of the main colors needed to keep a secondary color after it is found. 
When you form a color, remove both substrings. Otherwise, you should remove the last character of each substring and return them in the middle of the original string. If the string contains an odd number of substrings, you should put the substrings one position ahead.
For example, if you are given the string "re yellow bye" you could not form a color with the substring "re" and "bye", so you should remove the last character and return them in the middle of the string: "r by yellow".
In the end, print out the list with colors in the order in which they are found.

###Input
Single line string

###Output
The list with the collected colors

###Constrains
You will not receive an empty string
Please consider only the colors mentioned above
There won't be any cases with repeating colors