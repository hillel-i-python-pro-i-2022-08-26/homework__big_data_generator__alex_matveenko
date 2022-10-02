# Homework generate big data. Alex Matveenko

***

## Main commands

* `homework-i-run` - *run homework script*
* `init-dev` - *install requirements*
* `d-homework-i-run` - *run docker*
* `d-homework-i-purge` - *run all actions needed for purge project and related data*

## Create two function. Each with own way to generate data

1. `def big_data_generator__set` - *it use set to save data*
2. `def big_data_generator__list` - *it use list to save data*

#### Version with set (`def big_data_generator_set`):

* **Fast**
* **Excludes repetitions**
* **Passed 1_000_000 users generate**
* **function is generator that output info with `def output_data__set`**

#### Version with list (`def big_data_generator__list`):

* **Too slow**
* **Passed 200_000 users generate**
* **Return number of repeat login and password**
* **function is generator that output info with `def output_data__list`**