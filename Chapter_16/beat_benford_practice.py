"""Manipulate vote counts so that final results conform to Benford's Law."""

# example below is for Trump vs Clinton, Illinois, 2016 Presidental Election

def load_data(filename):
    """Open a text file of numbers & turn contents into a list of integers."""
    with open(filename) as f:
        lines = f.read().strip().split('\n')
        return [int(i) for i in lines]  # turn strings to integers

def steal_votes(opponent_votes, candidate_votes, scalar):
    """Use scalar to reduce one vote count & increase another, return as lists.

    Arguments:
    opponent_votes – votes to steal from
    candidate_votes - votes to increase by stolen amount
    scalar - fractional percentage, < 1, used to reduce votes

    Returns:
    list of changed opponent votes
    list of changed candidate votes
    
    """   
    new_opponent_votes = []
    new_candidate_votes = []
    for opp_vote, can_vote in zip(opponent_votes, candidate_votes):
        new_opp_vote = round(opp_vote * scalar)
        new_opponent_votes.append(new_opp_vote)
        stolen_votes = opp_vote - new_opp_vote
        new_can_vote = can_vote + stolen_votes
        new_candidate_votes.append(new_can_vote)
    return new_opponent_votes, new_candidate_votes
    

def main():
    """Run the program.

    Load data, set target winning vote count, call functions, display
    results as table, write new combined vote total as text file to
    use as input for Benford's Law analysis.

    """
    # load vote data
    c_votes = load_data('Clinton_votes_Illinois.txt')
    j_votes = load_data('Johnson_votes_Illinois.txt')
    s_votes = load_data('Stein_votes_Illinois.txt')
    t_votes = load_data('Trump_votes_Illinois.txt')

    total_votes = sum(c_votes + j_votes + s_votes + t_votes)


    # assume Trump amasses a plurality of the vote with 49%
    t_target = round(total_votes * 0.49)
    print("\nTrump winning target = {:,} votes".format(t_target))

    # calculate extra votes needed for Trump victory
    extra_votes_needed = abs(t_target - sum(t_votes))
    print("extra votes needed = {:,}".format(extra_votes_needed))

    # calculate scalar needed to generate extra votes
    scalar = 1 - (extra_votes_needed / sum(c_votes + j_votes + s_votes))
    print("scalar = {:.3}".format(scalar))
    print()

    # flip vote counts based on scalar & build new combined list of votes
    fake_counts = []
    new_c_votes, new_t_votes = steal_votes(c_votes, t_votes, scalar)
    fake_counts.extend(new_c_votes)
    new_j_votes, new_t_votes = steal_votes(j_votes, new_t_votes, scalar)
    fake_counts.extend(new_j_votes)
    new_s_votes, new_t_votes = steal_votes(s_votes, new_t_votes, scalar)
    fake_counts.extend(new_s_votes)
    fake_counts.extend(new_t_votes)  # add last as has been changing up til now   

    # compare old and new vote counts & totals in tabular form
    # switch-out "Trump" and "Clinton" as necessary
    for i in range(0, len(t_votes)):
        print("old Trump: {} \t new Trump: {} \t old Clinton: {} \t " \
              "new Clinton: {}".
              format(t_votes[i], new_t_votes[i], c_votes[i], new_c_votes[i]))              
        print("-" * 95)
    print("TOTALS:")
    print("old Trump: {:,} \t new Trump: {:,} \t old Clinton: {:,}  " \
          "new Clinton: {:,}".format(sum(t_votes), sum(new_t_votes),
                                     sum(c_votes), sum(new_c_votes)))
                                   
    # write-out a text file to use as input to benford.py program
    # this program will check conformance of faked votes to Benford's Law
    with open('fake_Illinois_counts.txt', 'w') as f:
        for count in fake_counts:
            f.write("{}\n".format(count))
    

if __name__ == '__main__':
    main()
