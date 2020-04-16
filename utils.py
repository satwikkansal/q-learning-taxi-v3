def select_optimal_action(q_table, state, action_space):
    max_q_value_action = None
    max_q_value = 0

    if q_table[state]:
        for action, action_q_value in q_table[state].items():
            if action_q_value >= max_q_value:
                max_q_value = action_q_value
                max_q_value_action = action

    return max_q_value_action if max_q_value_action else action_space.sample()
