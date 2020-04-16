# q-learning-taxi-v3

Table based q-learning implementation for taxi-v3 environment of Open AI gym.

## Instructions to run

```shell script
$ pip install -r requirements.txt
```

### Training
```shell script
$ python train.py --help
Usage: train.py [OPTIONS]

Options:
  --num-episodes INTEGER  Number of episodes to train on  [default: 100000]
  --save-path TEXT        Path to save the Q-table dump  [default:
                          q_table.pickle]
  --help                  Show this message and exit.
```

### Evaluation

```shell script
$ python evaluate.py --help
Usage: evaluate.py [OPTIONS]

Options:
  --num-episodes INTEGER  Number of episodes to train on  [default: 100]
  --q-path TEXT           Path to read the q-table values from  [default:
                          q_table.pickle]
  --help                  Show this message and exit.
```