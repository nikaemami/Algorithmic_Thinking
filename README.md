# Algorithmic_Thinking
Implementation of 3 different programs for the concept of **algorithmic thinking** in data structure projects.


<h2>Idle Monarch:</h2>

n numbers are available in a list. In each turn a new list is generated where the ith index in a list is the **number of its repetitions**.

For example, if the initial array is 4 4 4 2 2 2 3 3 1 1:

After the first iteration: 3 3 3 3 3 3 2 2 2 2

After the second iteration: 6 6 6 6 6 6 4 4 4 4

Now the idle monarch has q questions. In the jth question, he wants to know if the operation is done for Cj times, what the number in the Dj index is going to be.

<h4>INPUT:</h4>

Two numbers n, and q in the first line are given. In the next line, n input numbers are given, where the ith number is ai. In the jth line of the next q lines, Cj and Dj are given.

<h4>OUTPUT:</h4>

q numbers should be printed, where the jth number is the answer to the monarch's qj question.

Examples of input and output:

**INPUT**

3 10

4 4 4 2 2 2 3 3 1 1 1 1

2 3

2 7

**OUPUT**

3

6

4

In the code above, the most important part is the function which calculates the count of each digit:

```ruby
def counted_array (num_list,n)
```

The above function is called **q times** to find the answer.

<h2>Diet Plan:</h2>

A person wants to give his chef a diet for the next n days, where in the **jth day**, he has only **Ij options** for his meals. He has to choose exactly 1 meal for each day. He also wants to consume a lot of nutrients, so he doesn't want to eat **more than n/2 times** of a meal, in these n days of his diet.

INPUT: In the first line, a single number of n is given. In the jth line of the next n lines, first a single number of Ij is given. Then, Ij numbers (showing the types of meals he can choose from for the ith day) are given.

OUTPUT: If the condition was not satisfied, print "NO", else print "Yes", and in the next line, print n numbers where the ith index, is the type of meal chosen in the ith day.

**INPUT**

4

2 1 2

2 2 3

2 2 1

2 1 2

**OUPUT**

YES

1 3 1 2

Counting the number of meals and checking the considitions to make the decision is the key in this problem.

The two main conditions are as below:

```ruby
while (choose_cond == 0 and element < i ):
                if(count_dict[plan[j][element]]+1 <= math.floor(n/2)):
                  count=choice_dict[plan[j][element]]
                  possible_plan[j]=plan[j][element]
                  choice_dict[plan[j][element]]-=1
                  count_dict[plan[j][element]]+=1
                  choose_cond=1
```

```ruby
if (choice_dict[plan[j][k]] > count and (count_dict[plan[j][k]]+1) <= math.floor(n/2)):
                     possible_plan[j]=plan[j][k]
                     choice_dict[plan[j][element]]+=1
                     choice_dict[plan[j][k]]-=1
                     count_dict[plan[j][element]]-=1
                     count_dict[plan[j][k]]+=1
```

<h2>The Palindrome:</h2>

Converting a word to a **palindrome string** with taking the fewest actions possible.

In each action, one letter can be converted to another letter in the alphabet. Another important thing to know is that with taking the fewest actions for converting the word, how many different palindrome strings can be made.

INPUT: a string S that **needs to be converted** is given.

OUTPUT: in a single line, first print n, for the **minimum** number of conversions, then print the **remainder** of the number of possible strings to 10**9+7.

**INPUT**: abbc

**OUPUT**: 1 2

The important condition to be considered is as follows:

```ruby
if word[i] != word[len(word)-i-1]:
        count+=1
        count_2=2*count_2
        count_2=count_2%(10**9+7)
```

