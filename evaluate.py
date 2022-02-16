import pickle


import click
import gym

from utils import select_optimal_action


NUM_EPISODES = 100


def evaluate_agent(q_table, env, num_trials):
    total_epochs, total_penalties = 0, 0

    print("Running episodes...")
    for _ in range(num_trials):
        state = env.reset()
        epochs, num_penalties, reward = 0, 0, 0

        while reward != 20:
            next_action = select_optimal_action(q_table,state)
            state, reward, _, _ = env.step(next_action)

            if reward == -10:
                num_penalties += 1

            epochs += 1

        total_penalties += num_penalties
        total_epochs += epochs

    average_time = total_epochs / float(num_trials)
    average_penalties = total_penalties / float(num_trials)
    print("Evaluation results after {} trials".format(num_trials))
    print("Average time steps taken: {}".format(average_time))
    print("Average number of penalties incurred: {}".format(average_penalties))


@click.command()
@click.option('--num-episodes', default=NUM_EPISODES, help='Number of episodes to train on', show_default=True)
@click.option('--q-path', default="q_table.pickle", help='Path to read the q-table values from', show_default=True)
def main(num_episodes, q_path):
    env = gym.make("Taxi-v3")
    with open(q_path, 'rb') as f:
        q_table = pickle.load(f)
    evaluate_agent(q_table, env, num_episodes)


if __name__ == "__main__":
    main()
