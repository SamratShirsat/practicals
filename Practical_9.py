def activity_selection(start, finish):
    # Number of activities
    n = len(start)

    # Step 1: Sort activities by finish time
    activities = sorted(zip(start, finish, range(1, n + 1)), key=lambda x: x[1])

    # Print sorted activities
    print("\nSorted activities by finish time (Activity, Start, Finish):")
    for activity in activities:
        print(f"A{activity[2]}: Start: {activity[0]}, Finish: {activity[1]}")

    # Store the first selected activity
    selected_activities = []
    last_finish_time = -1  # Initially, no activity has been selected

    print("\nActivity Selection Process:")
    # Step 2: Iterate through sorted activities and select the ones that don't overlap
    for activity in activities:
        # If the start time of the current activity is >= finish time of last selected
        if activity[0] >= last_finish_time:
            selected_activities.append(activity)
            last_finish_time = activity[1]
            print(f"Selected activity: A{activity[2]}: Start: {activity[0]}, Finish: {activity[1]}")

    # Final selected activities
    print("\nFinal selected activities:")
    for activity in selected_activities:
        print(f"A{activity[2]}: Start: {activity[0]}, Finish: {activity[1]}")

    # Print the total number of selected activities
    print(f"\nTotal number of activities that can be selected: {len(selected_activities)}")


# Function to take user input for start and finish times as space-separated values
def get_user_input():
    start_times = list(map(int, input("Enter space-separated start times: ").split()))
    finish_times = list(map(int, input("Enter space-separated finish times: ").split()))
    return start_times, finish_times


# Main function to run the program
def main():
    start_times, finish_times = get_user_input()
    activity_selection(start_times, finish_times)


# Run the program
if __name__ == "__main__":
    main()