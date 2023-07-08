import random
import info
import art

print(art.logo)

score = 0
is_continue = False


def win():
    print(f"You are right! your current score is: {score}. Next ↓")


def lost():
    print(
        f"Sorry. You are wrong, your final score is: {score}.\n{compare_A['name']} has {A_follower_count}K followers and {against_A['name']} has {B_follower_count}K followers.")


while not is_continue:
    compare_A = random.choice(info.data)
    against_A = random.choice(info.data)
    print(f"\nCompare: {compare_A['name']}, a {compare_A['description']} from {compare_A['country']}.")
    print(art.vs)
    print(f"Against: {against_A['name']}, a {against_A['description']} from {against_A['country']}.")

    A_follower_count = compare_A["follower_count"]
    B_follower_count = against_A["follower_count"]

    user_input = input(f"\nWho has more followers? A) {compare_A['name']} or B) {against_A['name']}: ").lower()
    if user_input == "a":
        if A_follower_count >= B_follower_count:
            score += 1
            win()
        else:
            lost()
            is_continue = True

    elif user_input == "b":
        if B_follower_count >= A_follower_count:
            score += 1
            win()
        else:
            lost()
            is_continue = True
    else:
        print("\nPlease enter correct letter.")
        is_continue = True
