import streamlit as st
import numpy as np
import random

st.title('Tic Tac Toe Against AI')

# Reset the game
def reset_game():
    st.session_state.victory = 0
    st.session_state.game = np.zeros((3, 3), dtype=int)  # Initialize 3x3 board with zeros
    st.session_state.current_player = 1  # Player 1 starts (Human)
    st.session_state.turn_message = "Your Turn"  # Start with player's turn

st.button('Reset game', on_click=reset_game)

# Check for a winner
def check_win(board):
    # Check rows
    for i in range(3):
        if all(board[i][j] == 1 for j in range(3)):
            return 1
        if all(board[i][j] == 2 for j in range(3)):
            return 2

    # Check columns
    for j in range(3):
        if all(board[i][j] == 1 for i in range(3)):
            return 1
        if all(board[i][j] == 2 for i in range(3)):
            return 2

    # Check main diagonal
    if all(board[i][i] == 1 for i in range(3)):
        return 1
    if all(board[i][i] == 2 for i in range(3)):
        return 2

    # Check reverse diagonal
    if all(board[i][2 - i] == 1 for i in range(3)):
        return 1
    if all(board[i][2 - i] == 2 for i in range(3)):
        return 2

    # Check for a tie
    if all(board[i][j] != 0 for i in range(3) for j in range(3)):
        return -1

    return 0


# AI chooses a random available move
def ai_move(board):
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]
    if available_moves:
        move = random.choice(available_moves)
        board[move[0]][move[1]] = 2  # AI is player 2
    return board

# Initialize the game
def initialize():
    if 'color1' not in st.session_state:
        st.session_state.color1 = '#3A5683'
        st.session_state.alpha1 = 255
    if 'color2' not in st.session_state:
        st.session_state.color2 = '#73956F'
        st.session_state.alpha2 = 255
    if 'game' not in st.session_state:
        st.session_state.player1 = 'Player 1'
        st.session_state.player2 = 'AI'
        st.session_state.game = np.zeros((3, 3), dtype=int)  # Initialize 3x3 board with zeros
        st.session_state.victory = 0
        st.session_state.current_player = 1  # Player 1 (Human) starts
        st.session_state.turn_message = "Your Turn"

initialize()

# Check victory status
st.session_state.victory = check_win(st.session_state.game)

# Display current turn message
if st.session_state.victory == 0:
    st.subheader(st.session_state.turn_message)

# If the game is still ongoing, play the next turn
if st.session_state.victory == 0:
    for i in range(3):
        cols = st.columns(3)  # Create columns for the board
        for j in range(3):
            button_label = st.session_state.game[i][j]  # Display 0, 1, or 2 in the button
            if button_label == 0:
                button_label = "-"
            elif button_label == 1:
                button_label = "X"
            elif button_label == 2:
                button_label = "O"
            with cols[j]:
                if st.button(button_label, key=f'button_{i}_{j}', disabled=st.session_state.game[i][j] != 0 or st.session_state.victory != 0):
                    if st.session_state.victory == 0 and st.session_state.game[i][j] == 0:
                        st.session_state.game[i][j] = 1  # Human player is 1 (X)
                        st.session_state.victory = check_win(st.session_state.game)  # Check for human victory

                        # Check after the player's move
                        if st.session_state.victory == 0:  # If no one has won yet, AI takes its turn
                            st.session_state.turn_message = "AI's Turn"
                            # AI's move
                            st.session_state.game = ai_move(st.session_state.game)
                            st.session_state.victory = check_win(st.session_state.game)  # Check for AI victory
                            # After AI move, switch back to player's turn
                            if st.session_state.victory == 0:
                                st.session_state.turn_message = "Your Turn"

# If the game is over, display the result
if st.session_state.victory == 1:
    st.snow()  # Player 1 wins
    st.success('Player 1 wins!')
elif st.session_state.victory == 2:
    st.balloons()  # AI wins
    st.error('AI wins!')
elif st.session_state.victory == -1:
    st.success("It's a tie! Please click reset to play again.")
