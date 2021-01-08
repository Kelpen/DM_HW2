import numpy as np
import Information
import Data


def growing_or_stop():
    return


def should_i_check_this_subtree():
    return


# score function can be gini or entropy
def get_score_by_count(data_all, pos_all, data_less, pos_less, score_function):
    left_pos_prob = pos_less / data_less
    left_prob = (left_pos_prob, 1-left_pos_prob)

    right_pos_prob = (pos_all-pos_less) / (data_all-data_less)
    right_prob = (right_pos_prob, 1-right_pos_prob)

    less_then_prob = data_less / data_all

    score = less_then_prob * score_function(left_prob) + (1-less_then_prob) * score_function(right_prob)
    return score


# Input:
#   data: 2-D numpy array, each row is a sample.
#         The last column should be the target! 0: neg, 1: pos
#   available_features: Available feature index record in a list.
# Output:
#   Feature's id and separate score.
#   If no suitable split is found, return None.
def find_best_split(data, available_features):
    # iterate all feature
    #   iterate all values
    #     should_i_check_this_subtree()
    #     find best by score functions
    # growing_or_stop()

    all_data_num = data.shape[0]
    all_positive_num = np.sum(data[:, -1])

    pos_prob = all_positive_num / all_data_num
    score_init = Information.entropy((pos_prob, 1-pos_prob))

    best_gain = 0
    best_feature = None
    best_value = None

    # iterate all feature
    for f_id in available_features:
        feature_of_data = data[:, f_id]
        arg_sorted_foa = np.argsort(feature_of_data)

        # iterate all values
        separate_value = None
        pos_count = 0  # positive sample with feature value 'less then' the separate value
        data_count = 0  # all data ......

        for data_index in arg_sorted_foa:
            current_value = data[data_index, f_id]
            # print(data[data_index, f_id], data[data_index, -1])

            if separate_value is None:  # First
                separate_value = current_value

            elif current_value > separate_value:  # New separate point
                separate_value = current_value
                # use this split value to check score
                score = get_score_by_count(all_data_num, all_positive_num, data_count, pos_count, Information.entropy)
                print(separate_value, pos_count, data_count, score)
                gain = score_init - score
                if gain > best_gain:
                    best_gain = gain
                    best_feature = f_id
                    best_value = separate_value

            # counters
            if data[data_index, -1] == 1:
                pos_count += 1
            data_count += 1
    return best_feature, best_value


# similar to find_best_split
# only separate by feature == target
def find_best_split_discrete(data, available_features):
    return


# data structure
class Tree:
    def __init__(self):
        self.left_subtree: Tree
        self.right_subtree: Tree
        self.split_feature: int
        self.split_value: int

    def classify(self, data):
        return


if __name__ == '__main__':
    data_info, data_tpr = Data.read_xlsx('Training data.xlsx')
    bf, bv = find_best_split(data_info, [2])
    print(bf, bv)
