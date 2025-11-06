import random
# Set the number of candidates
N = 10
candidates = [{"id": i, "quality": random.randint(0, 100)} for i in
range(N)]
def hire_candidates(threshold):
 print("\nCandidates:")
 for candidate in candidates:
    print(f"[id: {candidate['id']}, quality:{candidate['quality']}]")

 hired = None
 for candidate in candidates:
    if candidate['quality'] >= threshold:
        hired = candidate
    break # Hire the first candidate who meets the threshold

 if hired:
    print("\nHired Candidate:")
    print(f"[id: {hired['id']}, quality: {hired['quality']}]")
 else:
    print("\nNo candidate meets the threshold.")
# Main program
try:
 # Take threshold input from the user
 threshold = int(input("Enter threshold (0-100): "))
 if 0 <= threshold <= 100:
    hire_candidates(threshold)
 else:
    print("Please enter a threshold between 0 and 100.")
except ValueError:
 print("Invalid input. Please enter a numeric value.")

 import random
# Set the number of candidates
N = 10
candidates = [{"id": i, "quality": random.randint(0, 100)} for i in
range(N)]
def hire_candidates(num_to_reject):
 rejected_candidates = candidates[:num_to_reject]
 if rejected_candidates:
    threshold = max(candidate['quality'] for candidate in
rejected_candidates)
 else:
    threshold = 0
 print(f"\nQuality threshold set to: {threshold}")
 remaining_candidates = candidates[num_to_reject:]
 print("\nRejected Candidates:")
 for candidate in rejected_candidates:
    print(f"[id: {candidate['id']}, quality:{candidate['quality']}]")
 print("\nRemaining Candidates (Eligible for Hiring):")
 for candidate in remaining_candidates:
     print(f"[id: {candidate['id']}, quality:{candidate['quality']}]")

 hired = None

 for candidate in remaining_candidates:
    if candidate['quality'] >= threshold:
        hired = candidate
        break # Hire the first candidate who meets or exceeds the threshold
 if hired:
    print("\nHired Candidate:")
    print(f"[id: {hired['id']}, quality: {hired['quality']}]")
 else:
    print("\nNo candidate meets the threshold.")
    print(f"Number of candidates: {len(candidates)}")
try:
 num_to_reject = int(input("\nEnter the number of candidates toreject: "))
 if 0 <= num_to_reject <= N:
    hire_candidates(num_to_reject)
 else:
    print(f"Please enter a number between 0 and {N}.")
except ValueError:
 print("Invalid input. Please enter a numeric value.")


 import random
# Set the number of candidates
N = 10
candidates = [{"id": i, "quality": random.randint(0, 100)} for i in
range(N)]
def hire_candidates(num_to_reject):
 rejected_candidates = candidates[:num_to_reject]
 if rejected_candidates:
   threshold = max(candidate['quality'] for candidate in
rejected_candidates)
 else:
   threshold = 0
 print(f"\nQuality threshold set to: {threshold}")
 remaining_candidates = candidates[num_to_reject:]
 print("\nRejected Candidates:")
 for candidate in rejected_candidates:
   print(f"[id: {candidate['id']}, quality:{candidate['quality']}]")
 print("\nRemaining Candidates (Eligible for Hiring):")
 for candidate in remaining_candidates:print(f"[id: {candidate['id']}, quality:{candidate['quality']}]")
 hired = None
 for candidate in remaining_candidates:
   if candidate['quality'] >= threshold:
      hired = candidate
      break # Hire the first candidate who meets or exceeds the threshold
 if hired:
   print("\nHired Candidate:")
   print(f"[id: {hired['id']}, quality: {hired['quality']}]")
 else:
   print("\nNo candidate meets the threshold.")
 
print(f"Number of candidates: {len(candidates)}")
try:
 num_to_reject = int(input("\nEnter the number of candidates to reject: "))
 if 0 <= num_to_reject <= N:
   hire_candidates(num_to_reject)
 else:
    print(f"Please enter a number between 0 and {N}.")
except ValueError:
 print("Invalid input. Please enter a numeric value.")
