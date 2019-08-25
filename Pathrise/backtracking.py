# What is backtracking? It's recursion, build one part of a solution at a time
#  Intelligent brute force

#  codingbat.com - Java - Recursion 1 & 2 - just do it in JS

#  Find what choices we have at each 

def backtracking_template(choices, other_params):
   if no_more_choices(): # Base Case
      return whether_or_not_the_problem_was_solvable
   else:
      for choice in choices:
         # edit choice or other_params to try out the choice
         if is_valid(choice):
            if choice_leads_to_a_success():
               return success 
   return failure

def backtracking_template(choices, other_params):
   if base_case():
      return whether_or_not_the_problem_was_solvable
   else:
      for choice in choices:
         # edit choice or other_params to try out the choice
         if is_valid(choice) && backtracking_template(choices, other_params):
            return success 
   return failure

