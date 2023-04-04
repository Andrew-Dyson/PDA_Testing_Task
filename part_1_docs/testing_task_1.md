### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:
      # the above line should use the equality operator == rather than =
      return True
    else
    # there should be colon at the end of else
      return False
   

  dif highest_card(self, card1 card2):
  # the above line should start with def not dif and there should be a comma after card1 in the parameters
  if card1.value > card2.value:
    return card
  # the line above should return card1
  else:
    return card2
  # line 31 onwards should be indented
  


def cards_total(self, cards):
  total
  # total variable needs to be assigned a value before use in the conditional statement
  for card in cards:
    total += card.value
    return "You have a total of" + total
    # need to create a formated string in line 45 as cannot concatinate string and int as it is
  
```
