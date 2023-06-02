def evaluate_guess(correct_word, guess_word):
    '''
    evaluate_guess(guess_word, correct_word)
    
        Evaluate a Wordle guess for correctness.
    
        Parameters
        ----------
        guess_word : str
            Guessed word for the Wordle puzzle.
            Must have same length as `correct_word`.
        correct_word : str
            Correct word for the Wordle puzzle
        
        Returns
        -------
        evaluation : list
            List whose entries indicate the correctness
            of the letters in `guess_word`.
            A `0` indicates that the letter in the
            corresponding index does not appear in 
            `correct_word` (gray tile).
            A `1` indicates that the letter in the 
            corresponding index appears in a different
            position in `correct_word` (yellow tile).
            A `2` indicates that the letter in the 
            corresponding index appears in the same
            position in `correct_word` (green tile).
    '''
    num_letters = len(correct_word)
    evaluation = [0 for i in range(num_letters)]
    remaining_letters = list(correct_word)
    for i,(correct_letter,guess_letter) in enumerate(zip(correct_word,guess_word)):
        if guess_letter == correct_letter:
            evaluation[i] = 2
            remaining_letters.remove(guess_letter)
    for i,(correct_letter,guess_letter) in enumerate(zip(correct_word,guess_word)):
        if guess_letter != correct_letter and guess_letter in remaining_letters:
            evaluation[i] = 1
            remaining_letters.remove(guess_letter)
    return evaluation

class wordle_game:
    '''
    A class to play Wordle in Jupyter notebook.
    
    ...
    
    Attributes
    ----------
    words : list
        A list of strings containing acceptable words.
        
    seed : int
        An integer that determines which word will be 
        chosen as correct. If none is provided, it will 
        be chosen randomly.
        
    correct_word : str
        The correct word for the Wordle puzzle.
    
    Methods
    -------
    play(num_guess=6)
        Plays wordle. The user will be prompted to enter
        their guesses, with a Matplotlib figure updating
        after each guess. 
    '''

    def __init__(self,words,seed=None):
        '''
            Parameters
            ----------
            words : list
                A list of strings containing acceptable words.
            seed : int, optional
                An integer that determines which word will be 
                chosen as correct. If none is provided, it 
                will be chosen randomly.
        '''
        import random
        self.words = words
        if seed is None:
            seed = random.randrange(len(words))
        self.seed = seed
        self.correct_word = words[seed]
        
    def play(self,num_guesses=6):
        '''
        Plays Wordle.
        
        Parameters
        ----------
        num_guesses: int, optional
            The number of guesses allowed. The default choice
            allows for six guesses.
        '''
        
        import matplotlib.pyplot as plt
        from matplotlib.patheffects import withStroke
        
        correct_word = self.correct_word
        num_letters = len(correct_word)
        words = self.words

        fig,ax = plt.subplots(figsize=((num_letters+1)*.7,(num_guesses)*.7))

        ax.axis('off')
        ax.set_aspect('equal')

        ax.set_xlim((-1,num_letters))
        ax.set_ylim((0,num_guesses))

        color_dict = {2:'green',
                      1:'yellow',
                      0:'gray'}

        for i in range(num_guesses):
            ax.text(-.5,num_guesses-i-.5,str(i+1),fontsize=20,ha='center',va='center')
            for j in range(num_letters):
                ax.fill_between([j,j+1],
                                [num_guesses-i-1,num_guesses-i-1],
                                [num_guesses-i,num_guesses-i],
                                color='k',alpha=.8,zorder=1)
        fig.tight_layout()
        fig.canvas.draw()
            
        for i in range(num_guesses):
            guess_word = input('Enter your guess ({} letters): '.format(num_letters)).upper()
            while guess_word not in words:
                guess_word = input('Invalid word. Enter your guess ({} letters): '.format(num_letters)).upper()
            evaluation = evaluate_guess(correct_word,guess_word)
            
            for j,(letter,n) in enumerate(zip(guess_word,evaluation)):
                color = color_dict[n]
                ax.fill_between([j,j+1],
                                [num_guesses-i-1,num_guesses-i-1],
                                [num_guesses-i,num_guesses-i],
                                color=color,alpha=.9,zorder=1)
                text = ax.text(j+.5,
                               num_guesses-i-.6,
                               letter,
                               color='w',fontsize=30,ha='center',va='center',zorder=11)
                text.set_path_effects([withStroke(linewidth=3,foreground='k')])
            
            fig.canvas.draw()
            
            if guess_word == correct_word:
                print('Correct!')
                plt.close(fig)
                return
        print('Better luck next time!')
        print('The correct word was "{}"'.format(correct_word))
        plt.close(fig)
        return
        

    