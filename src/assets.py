def fair_sharer(values, num_iterations, share=0.1):
    """
    Runs num_iterations.
    In each iteration the highest value in values gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neighbor of the rightmost field.
    """
    for _ in range(num_iterations):
        max_index = values.index(max(values))

        share_value = values[max_index] * share

        left_neighbor = (max_index - 1) % len(values)
        right_neighbor = (max_index + 1) % len(values)

        values[left_neighbor] += share_value
        values[right_neighbor] += share_value
        values[max_index] -= 2 * share_value

    return values

fair_sharer([0, 1000, 800, 0], 1)
fair_sharer([0, 1000, 800, 0], 2)

fair_sharer 
