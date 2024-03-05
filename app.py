import random

def simulate_loss_streak(total_bets, probability_of_loss):
    """
    Simulate the maximum loss streak based on the total number of bets and the probability of loss.
    """
    max_loss_streak = 0
    current_loss_streak = 0

    for _ in range(total_bets):
        if random.random() < probability_of_loss:  # Losing bet
            current_loss_streak += 1
            max_loss_streak = max(max_loss_streak, current_loss_streak)
        else:  # Winning bet
            current_loss_streak = 0

    return max_loss_streak


target = 2
total_bets = 100000
probability_of_win = round(1/target, 2)
probability_of_win -= 0.01  # 1% edge
probability_of_loss = 1 - probability_of_win
num_simulations = 100000

# Perform multiple simulations
total_max_loss_streaks = 0
max_loss_streak_across_simulations = 0
for i in range(num_simulations):
    max_loss_streak = simulate_loss_streak(total_bets, probability_of_loss)
    total_max_loss_streaks += max_loss_streak
    max_loss_streak_across_simulations = max(max_loss_streak_across_simulations, max_loss_streak)
    
    print(f"Simulation {i + 1}: Expected maximum loss streak: {max_loss_streak}")
    # print(f"Simulation {i + 1}: Expected maximum loss streak: {max_loss_streak}, probability_of_loss: {probability_of_loss}")

# Calculate and print the average maximum loss streak
average_max_loss_streak = total_max_loss_streaks / num_simulations
#print(f"Average maximum loss streak from {num_simulations} simulations: {average_max_loss_streak}")

# Print the maximum loss streak across all simulations
print(f"Maximum loss streak across all simulations: {max_loss_streak_across_simulations}")